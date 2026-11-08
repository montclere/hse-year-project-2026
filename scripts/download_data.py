"""Загрузка и первичная фильтрация данных проекта.

Запуск из корня репозитория:
    python scripts/download_data.py srd                 # SRD 5.1 в Markdown
    python scripts/download_data.py open5e              # Open5e, обе версии, JSON
    python scripts/download_data.py se-extract FILE.7z  # достать Posts.xml из дампа
    python scripts/download_data.py se-filter           # вопросы dnd-5e-2014/2024 -> jsonl

Повторный запуск не качает то, что уже лежит на диске (--force перекачивает).
Каждый источник записывается в data/raw/MANIFEST.json (url, лицензия, дата).
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
INTERIM = ROOT / "data" / "interim"
MANIFEST = RAW / "MANIFEST.json"

SRD_REPO = "https://github.com/gabrielrega/cc-srd5.git"

# Open5e API v2, параметры проверены 2026-11-06 (ключи документов см. /v2/documents/).
OPEN5E_BASE = "https://api.open5e.com/v2"
OPEN5E_VERSIONS = {"2014": "srd-2014", "2024": "srd-2024"}  # версия -> document key
OPEN5E_ENDPOINTS = ["spells", "classes", "creatures", "items", "magicitems", "weapons", "armor",
                    "feats", "backgrounds", "species", "rules"]
# Проверено 2026-11-06: именно __in даёт верную версию на всех эндпоинтах
# (document__key на items/magicitems возвращает не ту версию).
OPEN5E_FILTER_PARAM = "document__key__in"
OPEN5E_PAGE_SIZE = 100
# Условий (conditions) для srd-2014/srd-2024 в Open5e нет: они лежат в документе core (2014) и a5e-ag.
# Качаем без фильтра, версию определяет поле document.key.
OPEN5E_UNFILTERED = ["conditions"]

# В дампе rpg.stackexchange.com от апреля 2024 есть только тег dnd-5e (правила 2014);
# тегов dnd-5e-2014 / dnd-5e-2024 там нет. Для более нового дампа добавьте их сюда.
SE_TAGS = {"dnd-5e"}


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def record(name: str, **info) -> None:
    """Дописать источник в манифест (провенанс: откуда, когда, лицензия)."""
    RAW.mkdir(parents=True, exist_ok=True)
    data = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {}
    data[name] = {**info, "retrieved_at": now()}
    MANIFEST.write_text(json.dumps(data, ensure_ascii=False, indent=2))


def get_json(url: str, retries: int = 4, timeout: int = 60) -> dict:
    """GET с повторами и нарастающей паузой; ошибки не глотаем."""
    last: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "hse-year-project-2026"})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return json.load(resp)
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            last = exc
            wait = 2**attempt
            print(f"  попытка {attempt}/{retries} не удалась ({exc}); жду {wait} с", file=sys.stderr)
            time.sleep(wait)
    raise RuntimeError(f"не удалось получить {url}: {last}")


def cmd_srd(args: argparse.Namespace) -> None:
    dest = RAW / "srd-5.1"
    if dest.exists() and not args.force:
        print(f"[srd] уже есть: {dest}")
    else:
        if dest.exists():
            shutil.rmtree(dest)
        RAW.mkdir(parents=True, exist_ok=True)
        subprocess.run(["git", "clone", "--depth", "1", SRD_REPO, str(dest)], check=True)
    md = dest / "cc-srd5.md"
    if not md.exists():
        sys.exit(f"[srd] нет файла {md}: структура репозитория изменилась")
    record("srd-5.1", url=SRD_REPO, file=str(md.relative_to(ROOT)), license="CC BY 4.0",
           note="SRD 5.1 (правила 2014) в Markdown; защищённые термины заменены общими")
    print(f"[srd] готово: {md} ({md.stat().st_size / 1e6:.1f} МБ)")


def fetch_all(url: str) -> list[dict]:
    """Обойти пагинацию (поле next) и собрать results."""
    items: list[dict] = []
    while url:
        page = get_json(url)
        items.extend(page.get("results", []))
        url = page.get("next")
        print(f"  собрано {len(items)} из {page.get('count', '?')}")
    return items


def doc_key(item: dict) -> str | None:
    doc = item.get("document")
    return doc.get("key") if isinstance(doc, dict) else doc


def download_open5e(out: Path, url: str, label: str, expect_doc: str | None, force: bool) -> None:
    if out.exists() and not force:
        print(f"[open5e] уже есть: {out.relative_to(ROOT)}")
        return
    print(f"[open5e] {label}: {url}")
    try:
        items = fetch_all(url)
    except RuntimeError as exc:
        print(f"[open5e] ПРОПУЩЕНО: {exc}", file=sys.stderr)
        return
    if expect_doc:  # страховка от фильтра, который API молча проигнорировал
        wrong = [i for i in items if doc_key(i) != expect_doc]
        if wrong:
            print(f"[open5e] ОШИБКА {label}: {len(wrong)} из {len(items)} записей не из {expect_doc}; "
                  "файл не сохранён", file=sys.stderr)
            return
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(items, ensure_ascii=False))
    record(f"open5e/{label}", url=url, count=len(items), license="CC BY 4.0")


def cmd_open5e(args: argparse.Namespace) -> None:
    for version, key in OPEN5E_VERSIONS.items():
        for endpoint in OPEN5E_ENDPOINTS:
            url = f"{OPEN5E_BASE}/{endpoint}/?{OPEN5E_FILTER_PARAM}={key}&limit={OPEN5E_PAGE_SIZE}"
            download_open5e(RAW / "open5e" / version / f"{endpoint}.json", url,
                            f"{version}/{endpoint}", key, args.force)
    for endpoint in OPEN5E_UNFILTERED:
        url = f"{OPEN5E_BASE}/{endpoint}/?limit={OPEN5E_PAGE_SIZE}"
        download_open5e(RAW / "open5e" / "unfiltered" / f"{endpoint}.json", url,
                        f"unfiltered/{endpoint}", None, args.force)
    print("[open5e] готово, файлы в data/raw/open5e/")


def cmd_se_extract(args: argparse.Namespace) -> None:
    archive = Path(args.archive)
    if not archive.exists():
        sys.exit(f"нет файла {archive}")
    seven_zip = shutil.which("7z") or shutil.which("7zz")
    if not seven_zip:
        sys.exit("нужен 7z: brew install p7zip")
    dest = RAW / "stackexchange"
    dest.mkdir(parents=True, exist_ok=True)
    subprocess.run([seven_zip, "x", str(archive), f"-o{dest}", "Posts.xml", "-y"], check=True)
    record("stackexchange/Posts.xml", archive=archive.name, license="CC BY-SA",
           note="только Posts.xml из дампа rpg.stackexchange.com")
    print(f"[se-extract] готово: {dest / 'Posts.xml'}")


def parse_tags(raw: str) -> set[str]:
    """Теги из атрибута Tags. Дамп 2024 хранит '|dnd-5e|spells|', старые дампы '<dnd-5e><spells>'."""
    return {t for t in raw.replace("<", "|").replace(">", "|").split("|") if t}


def cmd_se_filter(args: argparse.Namespace) -> None:
    posts = Path(args.posts) if args.posts else RAW / "stackexchange" / "Posts.xml"
    if not posts.exists():
        sys.exit(f"нет файла {posts}; сначала se-extract")
    questions: dict[str, dict] = {}
    accepted: dict[str, str] = {}  # id вопроса -> текст принятого ответа
    # потоковое чтение: Posts.xml может быть очень большим.
    # Ответ всегда идёт после своего вопроса (больший Id), поэтому хватает одного прохода.
    for _, elem in ET.iterparse(posts, events=("end",)):
        if elem.tag != "row":
            continue
        a = elem.attrib
        if a.get("PostTypeId") == "1":
            tags = parse_tags(a.get("Tags", ""))
            if tags & SE_TAGS:
                questions[a["Id"]] = {
                    "id": a["Id"], "title": a.get("Title", ""), "body": a.get("Body", ""),
                    "tags": sorted(tags), "score": int(a.get("Score", 0)),
                    "created": a.get("CreationDate"), "accepted_answer_id": a.get("AcceptedAnswerId"),
                }
        elif a.get("PostTypeId") == "2":
            q = questions.get(a.get("ParentId", ""))
            if q and q["accepted_answer_id"] == a["Id"]:
                accepted[q["id"]] = a.get("Body", "")
        elem.clear()
    out = INTERIM / "se_questions.jsonl"
    INTERIM.mkdir(parents=True, exist_ok=True)
    with out.open("w") as f:
        for q in questions.values():
            q["accepted_answer"] = accepted.get(q["id"])
            f.write(json.dumps(q, ensure_ascii=False) + "\n")
    print(f"[se-filter] вопросов: {len(questions)}, с принятым ответом: "
          f"{sum(1 for q in questions.values() if q['accepted_answer'])} -> {out.relative_to(ROOT)}")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--force", action="store_true", help="перекачать, даже если файлы уже есть")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("srd").set_defaults(func=cmd_srd)
    sub.add_parser("open5e").set_defaults(func=cmd_open5e)
    sx = sub.add_parser("se-extract")
    sx.add_argument("archive")
    sx.set_defaults(func=cmd_se_extract)
    sf = sub.add_parser("se-filter")
    sf.add_argument("--posts", help="путь к Posts.xml (по умолчанию data/raw/stackexchange/Posts.xml)")
    sf.set_defaults(func=cmd_se_filter)
    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
