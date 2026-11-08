<div align="center">

<img src="docs/img/banner.svg" alt="RAG-система / дообучение LLM под домен" width="100%">

<img src="https://readme-typing-svg.demolab.com?font=Inconsolata&weight=600&size=26&duration=3200&pause=700&color=4C8DF6&center=true&vCenter=true&repeat=true&width=900&height=60&lines=%D0%A2%D0%BE%D1%87%D0%BD%D1%8B%D0%B5+%D0%BE%D1%82%D0%B2%D0%B5%D1%82%D1%8B+%D0%BF%D0%BE+%D0%B1%D0%BE%D0%BB%D1%8C%D1%88%D0%BE%D0%BC%D1%83+%D0%BA%D0%BE%D1%80%D0%BF%D1%83%D1%81%D1%83+%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%BE%D0%B2;Retrieval+%C2%B7+Generation+%C2%B7+Evaluation;%D0%9C%D0%B5%D0%BD%D1%8C%D1%88%D0%B5+%D0%B3%D0%B0%D0%BB%D0%BB%D1%8E%D1%86%D0%B8%D0%BD%D0%B0%D1%86%D0%B8%D0%B9+%E2%80%94+%D0%B1%D0%BE%D0%BB%D1%8C%D1%88%D0%B5+%D1%84%D0%B0%D0%BA%D1%82%D0%BE%D0%B2" alt="Точные ответы по большому корпусу документов · Retrieval · Generation · Evaluation" />

<br/>

![Status](https://img.shields.io/badge/status-in_progress-4C8DF6?style=flat-square)
![Level](https://img.shields.io/badge/level-PRO-1E50C8?style=flat-square)
![Task](https://img.shields.io/badge/task-QA_%2B_text_generation-0F2D69?style=flat-square)
![Year](https://img.shields.io/badge/%D0%B3%D0%BE%D0%B4%D0%BE%D0%B2%D0%BE%D0%B9_%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82-2026%E2%80%932027-0B1F4D?style=flat-square)

[**О проекте**](#-о-проекте) &nbsp;•&nbsp;
[**Команда**](#-команда) &nbsp;•&nbsp;
[**Стек**](#-планируемый-стек) &nbsp;•&nbsp;
[**План работы**](#-план-работы) &nbsp;•&nbsp;
[**Метрики**](#-метрики)

</div>

<img src="docs/img/divider.svg" alt="" width="100%">

## 📌 О проекте

**Тема:** RAG-система / дообучение LLM под домен. Домен: **AI-судья по правилам D&D 5e с учётом версий (2014 и 2024) и домашних правил**.

### Проблема

Игрокам и мастерам нужны точные ответы по правилам на сотнях страниц. Поиск по ключевым словам не связывает несколько правил, а LLM без контекста отвечает уверенно, но галлюцинирует: смешивает версии 2014 и 2024 (например, *Контрзаклинание* в 2014 автоматически отменяет заклинания до 3-го уровня, а в 2024 цель делает спасбросок Телосложения), выдумывает правила и подтягивает домашние правила с форумов.

### Цель

Система вопрос-ответ на русском по официальным правилам со ссылками на разделы и с указанием версии. На втором этапе система следует иерархии «хоумрулы стола → правила выбранной версии», даже если модель «знает» другой вариант.

### Задачи

- **Часть А (базовая, закрывает ТЗ):** сбор и подготовка корпуса, эмбеддинги и индекс, retrieval + генерация, тестсет с эталонами, оценка (RAGAS, human eval), сравнение RAG и LoRA, анализ галлюцинаций и adversarial-вопросов.
- **Часть Б (усложнения):** домашние правила, граф правил с версиями, агентный граф (LangGraph), верификатор утверждений, RAFT, калибровка LLM-судьи.

### Данные

| Источник | Что | Версия | Лицензия |
|---|---|---|---|
| SRD 5.1 (`gabrielrega/cc-srd5`), Markdown | Полный текст правил | 2014 | CC BY 4.0 |
| SRD 5.2.1, PDF → Markdown | Полный текст правил | 2024 | CC BY 4.0 |
| Open5e API v2 (`srd-2014`, `srd-2024`) | Сущности: заклинания, монстры, классы и др. (JSON) | обе | CC BY 4.0 |
| Дамп Stack Exchange `rpg.stackexchange.com` | 22 325 вопросов с тегом `dnd-5e` | 2014 | CC BY-SA |

Данные скачиваются скриптами, в git не хранятся. Результаты EDA: [EDA.ipynb](EDA.ipynb).

### Подход

Мультиязычные эмбеддинги (BGE-M3), гибридный поиск (dense + sparse) в Qdrant с фильтром по версии → реранкер → генерация open-source LLM 7–8B с обязательными ссылками на разделы. Бейзлайны: LLM без контекста и BM25. Далее LoRA/RAFT, граф правил и агентная система, каждое усложнение добавляется отдельно, чтобы его вклад был виден в абляции.

<img src="docs/img/divider.svg" alt="" width="100%">

## 👥 Команда

<div align="center">

<table>
  <tr>
    <td align="center" width="340">
      <br/>
      <img src="https://img.shields.io/badge/%D0%9A%D1%83%D1%80%D0%B0%D1%82%D0%BE%D1%80-0F2D69?style=for-the-badge" alt="Куратор" />
      <br/><br/>
      <b>Мовсумов Денис</b>
      <br/>
      <sub>Руководитель проекта</sub>
      <br/><br/>
    </td>
    <td align="center" width="340">
      <br/>
      <img src="https://img.shields.io/badge/%D0%A1%D1%82%D1%83%D0%B4%D0%B5%D0%BD%D1%82-1E50C8?style=for-the-badge" alt="Студент" />
      <br/><br/>
      <b>Армбристер Владислав</b>
      <br/>
      <sub>Исполнитель проекта</sub>
      <br/><br/>
      <a href="https://github.com/montclere"><img src="https://img.shields.io/badge/@montclere-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub @montclere" /></a>
      <br/><br/>
    </td>
  </tr>
</table>

</div>

<img src="docs/img/divider.svg" alt="" width="100%">

## 🧰 Планируемый стек

<div align="center">

<img src="https://skillicons.dev/icons?i=python,pytorch,fastapi,docker,git,github,linux&theme=dark&perline=7" alt="Python, PyTorch, FastAPI, Docker, Git, GitHub, Linux" />

<br/><br/>

![RAG](https://img.shields.io/badge/RAG-4C8DF6?style=flat-square)
![Embeddings](https://img.shields.io/badge/Embeddings-3A74E8?style=flat-square)
![Vector Search](https://img.shields.io/badge/Vector_Search-1E50C8?style=flat-square)
![Prompt Engineering](https://img.shields.io/badge/Prompt_Engineering-1A44A8?style=flat-square)
![LoRA](https://img.shields.io/badge/LoRA-0F2D69?style=flat-square)
![RAGAS](https://img.shields.io/badge/RAGAS-0B1F4D?style=flat-square)
<br/>
![Hugging Face](https://img.shields.io/badge/Hugging_Face-4C8DF6?style=flat-square&logo=huggingface&logoColor=white)
![Qdrant](https://img.shields.io/badge/Qdrant-3A74E8?style=flat-square)
![BGE-M3](https://img.shields.io/badge/BGE--M3-1E50C8?style=flat-square)
![LangGraph](https://img.shields.io/badge/LangGraph-1A44A8?style=flat-square)
![MLflow](https://img.shields.io/badge/MLflow-0F2D69?style=flat-square&logo=mlflow&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-0B1F4D?style=flat-square&logo=pandas&logoColor=white)

</div>

<img src="docs/img/divider.svg" alt="" width="100%">

## 📅 План работы

> Приблизительный план на учебный год — этапы и сроки будут уточняться вместе с куратором.

| Этап | Период | Что делаем | Результат |
|:----:|:------:|------------|-----------|
| **1** | Октябрь | **Постановка задачи.** Выбор домена (D&D 5e, две версии правил), согласование метрик | Описание проекта, репозиторий |
| **2** | Ноябрь | **Корпус и EDA (А1–А3).** Сбор SRD 2014/2024, Open5e, вопросов Stack Exchange; разведочный анализ; парсинг и чанкинг, индекс | `EDA.ipynb`, корпус, индекс |
| **3** | Ноябрь – декабрь | **RAG и оценка (А4–А6).** Гибридный поиск + реранкер + генерация, тестсет v1, RAGAS, бейзлайн «LLM без контекста»; FastAPI-сервис | MVP: требования ТЗ закрыты |
| **4** | Январь – февраль | **Сравнение и усложнения (А7–А8, Б1–Б4).** RAG против LoRA, галлюцинации и adversarial, хоумрулы, граф правил, агенты, верификатор | Агентная система, тестсет v2 |
| **5** | Март – апрель | **RAFT и эксперименты (Б5–Б6).** Сравнение RAG, LoRA, RAFT, RAG + RAFT; version leak rate, обновление знаний | Таблица сравнения вариантов |
| **6** | Май – июнь | **Финал (Б7).** Калибровка LLM-судьи, human eval, разбор провалов, MLflow и воспроизводимость, демо, отчёт, защита | Готовый проект |

### Чек-лист

- [x] Создан репозиторий проекта
- [x] Определены домен (D&D 5e, версии 2014 и 2024) и корпус документов
- [x] Данные собраны (SRD 5.1, SRD 5.2.1, Open5e, Stack Exchange)
- [x] Проведён разведочный анализ данных (чекпойнт 2): [EDA.ipynb](EDA.ipynb)
- [ ] Корпус очищен, разбит на чанки и проиндексирован
- [ ] Реализован baseline RAG
- [ ] Собран тестовый набор вопросов с эталонами
- [ ] Проведена оценка качества (RAGAS, human eval)
- [ ] Выполнено сравнение RAG vs fine-tuning
- [ ] Задокументированы неудачные ответы и меры по их снижению
- [ ] Подготовлена защита проекта

<img src="docs/img/divider.svg" alt="" width="100%">

## 📊 Метрики

> Целевые значения предварительные: пороги будут согласованы с куратором.

<div align="center">

| | 🎯 Faithfulness | 💬 Answer relevance | 🔎 Context precision / recall | 🧑‍⚖️ Human eval | ⏱ Latency |
|---|:---:|:---:|:---:|:---:|:---:|
| **Что показывает** | ответ опирается на найденные источники, без выдумок | ответ действительно отвечает на вопрос | насколько релевантны и полны найденные фрагменты | экспертная оценка ответов | время отклика системы |
| **Ориентир** | ≥ 0.85 | ≈ 0.8+ | ≈ 0.7+ | ≈ 4 / 5 | ≈ до 5 с |

</div>

**Критерии приёмки (предварительно)**

1. Корпус документов собран и проиндексирован.
2. Ответы на тестовом наборе вопросов оценены по релевантности и достоверности **выше согласованного порога** (ориентир: faithfulness ≥ 0.85, точность ≥ 70%, корректный отказ на ≥ 80% неотвечаемых вопросов).
3. Задокументированы случаи неудачных ответов и предложены меры их снижения.

Дополнительные метрики проекта: version leak rate (смешение 2014 и 2024), доля ложных отказов, hit@k / MRR поиска. Бейзлайн поиска: BM25 (результаты в [EDA.ipynb](EDA.ipynb)).

<img src="docs/img/divider.svg" alt="" width="100%">

## 📁 Структура репозитория

```
EDA.ipynb                  # разведочный анализ данных (чекпойнт 2)
docs/                      # ТЗ, чекпойнты, проектный план, практическая применимость
reports/                   # графики EDA и PDF о практической применимости
scripts/
  download_data.py         # загрузка SRD 5.1, Open5e, дампа Stack Exchange
  extract_srd_2024.py      # SRD 5.2.1: PDF -> Markdown с проверками
data/raw/                  # скачанные данные (не в git)
data/interim/              # очищенные данные (не в git)
```

## 🚀 Запуск

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt

# данные
.venv/bin/python scripts/download_data.py srd        # SRD 5.1 (Markdown)
.venv/bin/python scripts/download_data.py open5e     # Open5e, обе версии
# дамп rpg.stackexchange.com (archive.org) положить в data/raw/stackexchange/
.venv/bin/python scripts/download_data.py se-filter --posts data/raw/stackexchange/Posts.xml
# SRD 5.2.1 (PDF с dndbeyond.com/srd) -> data/raw/srd-5.2.1/SRD_CC_v5.2.1.pdf
.venv/bin/python scripts/extract_srd_2024.py

# анализ
.venv/bin/python -m nbconvert --to notebook --execute --inplace EDA.ipynb
```

<img src="docs/img/divider.svg" alt="" width="100%">

<div align="center">

<img src="docs/img/footer.svg" alt="RAG-система / дообучение LLM под домен" width="100%">

</div>
