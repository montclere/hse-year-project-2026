"""Извлечение текста из SRD 5.2.1 (PDF, правила 2024) в Markdown.

    .venv/bin/python scripts/extract_srd_2024.py

Подход: PyMuPDF + pymupdf4llm (порядок чтения в колонках, таблицы, курсив/жирный),
колонтитулы отбрасываем, уровни заголовков восстанавливаем по оглавлению PDF (закладкам),
а не по размеру шрифта. Результат проверяется по оглавлению PDF и по Open5e.

Выход: data/interim/srd_2024/srd_5.2.1.md и pages.jsonl (текст по страницам, для ссылок на страницу).
"""

from __future__ import annotations

import json
import re
import sys
import warnings
from pathlib import Path

import pymupdf
import pymupdf4llm

warnings.filterwarnings("ignore")

ROOT = Path(__file__).resolve().parent.parent
PDF = ROOT / "data" / "raw" / "srd-5.2.1" / "SRD_CC_v5.2.1.pdf"
OUT = ROOT / "data" / "interim" / "srd_2024"
OPEN5E = ROOT / "data" / "raw" / "open5e" / "2024"

TOC_PAGES = 4  # первые страницы: титул, лицензия, оглавление
HEAD = re.compile(r"^(#+) (.*)$")
# название заклинания, склеенное с курсивной подписью: **Acid SplASh** _Evocation Cantrip (...)_
INLINE_SPELL = re.compile(r"^\*\*(?P<name>[^*]+)\*\* (?P<sub>_(?:[A-Za-z]+ Cantrip|Level \d)[^_]*_)$")


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", s.lower().replace("’", "'")).strip()


def plain(title: str) -> str:
    return re.sub(r"</?u>|</?mark>|[*_]", "", title).strip()


def clean(text: str) -> str:
    text = text.replace("\u00ad", "")  # мягкие переносы
    text = re.sub(r"[ \t]+\n", "\n", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"


def nearby_toc(toc_by_page: dict[int, dict[str, int]], page: int) -> dict[str, int]:
    """Закладка может указывать на страницу раньше самого заголовка, поэтому берём соседние."""
    merged: dict[str, int] = {}
    for p in (page + 1, page - 1, page):  # приоритет у закладок текущей страницы
        merged.update(toc_by_page.get(p, {}))
    return merged


def restructure(text: str, toc_levels: dict[str, int], parent: int) -> tuple[str, int]:
    """Привести заголовки страницы к иерархии оглавления.

    Заголовок из оглавления получает его уровень (глава #, раздел ##, подраздел ###).
    Остальные (заклинания, предметы, метки статблоков) становятся дочерними текущего раздела.
    Заголовки шестого уровня в исходнике это подписи (тип предмета и т.п.), делаем обычным текстом.
    """
    out = []
    for line in text.split("\n"):
        m = INLINE_SPELL.match(line)
        if m:  # заголовок заклинания склеен с подписью (малые заглавные дают «SplASh»)
            name = m["name"].strip()
            if any(c.islower() for c in name) and re.search(r"[a-z][A-Z]", name):
                name = " ".join(w.capitalize() for w in name.split())
            out += [f"{'#' * min(parent + 1, 4)} {name}", "", m["sub"]]
            continue
        m = HEAD.match(line)
        if not m:
            out.append(re.sub(r"</?u>|</?mark>", "", line))
            continue
        title = plain(m.group(2))
        if norm(title) in toc_levels:
            parent = toc_levels[norm(title)]
            out.append(f"{'#' * parent} {title}")
        elif len(m.group(1)) >= 6:
            out.append(re.sub(r"</?u>|</?mark>", "", m.group(2)))
        else:
            out.append(f"{'#' * min(parent + 1, 4)} {title}")
    return "\n".join(out), parent


def main() -> None:
    if not PDF.exists():
        sys.exit(f"нет файла {PDF}: положите SRD_CC_v5.2.1.pdf в data/raw/srd-5.2.1/")
    doc = pymupdf.open(PDF)
    chunks = pymupdf4llm.to_markdown(doc, page_chunks=True, header=False, footer=False, show_progress=False)
    toc_by_page: dict[int, dict[str, int]] = {}
    for lvl, title, pno in doc.get_toc():
        if lvl >= 2:  # уровень 1 это название документа; глава ТОС 2 -> заголовок #
            toc_by_page.setdefault(pno, {})[norm(title)] = lvl - 1
    OUT.mkdir(parents=True, exist_ok=True)
    pages, parent = [], 1
    for i, ch in enumerate(chunks, start=1):
        if i <= TOC_PAGES:
            continue
        text, parent = restructure(clean(ch["text"]), nearby_toc(toc_by_page, i), parent)
        pages.append({"page": i, "text": clean(text)})
    with (OUT / "pages.jsonl").open("w") as f:
        for p in pages:
            f.write(json.dumps(p, ensure_ascii=False) + "\n")
    md = "\n".join(p["text"] for p in pages)
    (OUT / "srd_5.2.1.md").write_text(md)
    print(f"страниц: {len(pages)}, символов: {len(md)} -> {OUT.relative_to(ROOT)}")
    validate(doc, md)


def validate(doc: pymupdf.Document, md: str) -> None:
    """Проверки качества: заголовки из оглавления PDF и сущности Open5e должны находиться."""
    heads = [(len(m.group(1)), re.sub(r"[*_]", "", m.group(2)).strip()) for m in re.finditer(r"^(#+) (.*)$", md, re.M)]
    head_set = {norm(h) for _, h in heads}
    print("заголовков по уровням:", {lvl: sum(1 for l, _ in heads if l == lvl) for lvl in sorted({l for l, _ in heads})})
    toc = [t for lvl, t, p in doc.get_toc() if p > TOC_PAGES]
    miss = [t for t in toc if norm(t) not in head_set]
    print(f"оглавление PDF: найдено как заголовки {len(toc) - len(miss)}/{len(toc)}; нет: {miss[:12]}")
    for name, fname in [("заклинания", "spells.json"), ("монстры", "creatures.json")]:
        path = OPEN5E / fname
        if not path.exists():
            print(f"{name}: нет {path.name}, сверка пропущена")
            continue
        names = [x["name"] for x in json.load(path.open())]
        miss = [n for n in names if norm(n) not in head_set]
        print(f"Open5e {name}: найдено как заголовки {len(names) - len(miss)}/{len(names)}; нет: {miss[:12]}")
    leftovers = len(re.findall(r"System Reference Document 5\.2\.1", md))
    print(f"остатков колонтитула в тексте: {leftovers}")


if __name__ == "__main__":
    main()
