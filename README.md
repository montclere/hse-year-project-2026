<div align="center">

<img src="docs/img/banner.svg" alt="RAG-система / дообучение LLM под домен" width="100%">

<br>

**Вопросно-ответная система по корпусу документов: точные ответы, ссылки на источники и борьба с галлюцинациями**

![Status](https://img.shields.io/badge/status-in%20progress-yellow?style=for-the-badge)
![Level](https://img.shields.io/badge/level-PRO-red?style=for-the-badge)
![Task](https://img.shields.io/badge/task-QA%20%2B%20text%20generation-blue?style=for-the-badge)

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![LLM](https://img.shields.io/badge/LLM-open--source-8A2BE2)
![Vector Store](https://img.shields.io/badge/Vector%20store-FAISS%20%7C%20Qdrant%20%7C%20Chroma-009688)
![LoRA](https://img.shields.io/badge/Fine--tuning-LoRA-orange)
![RAGAS](https://img.shields.io/badge/Eval-RAGAS-success)

[О проекте](#-о-проекте) •
[Команда](#-команда) •
[Стек](#-планируемый-стек) •
[План работы](#-план-работы) •
[Метрики](#-метрики)

</div>

<img src="docs/img/divider.svg" alt="" width="100%">

## 📌 О проекте

**Тема:** RAG-система / дообучение LLM под домен

### Проблема

> 🚧 _Раздел в разработке_

### Цель

> 🚧 _Раздел в разработке_

### Задачи

> 🚧 _Раздел в разработке_

### Данные

> 🚧 _Раздел в разработке_

### Подход

> 🚧 _Раздел в разработке_

<img src="docs/img/divider.svg" alt="" width="100%">

## 👥 Команда

| | Роль | ФИО | GitHub |
|:-:|------|-----|--------|
| 🧑‍🏫 | **Куратор** | _ФИО куратора_ | — |
| 🧑‍💻 | **Студент** | _ФИО_ | [@ArmbristerVlad](https://github.com/ArmbristerVlad) |

<!-- TODO: указать ФИО куратора и своё -->

<img src="docs/img/divider.svg" alt="" width="100%">

## 🧰 Планируемый стек

| Направление | Инструменты |
|-------------|-------------|
| **Язык и ML** | ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) ![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch&logoColor=white) ![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FFD21E?logo=huggingface&logoColor=black) ![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white) |
| **RAG** | ![RAG](https://img.shields.io/badge/RAG-4C8DF6) ![Embeddings](https://img.shields.io/badge/Embeddings-1E50C8) ![Vector Search](https://img.shields.io/badge/Vector%20Search-0F2D69) ![Prompt Engineering](https://img.shields.io/badge/Prompt%20Engineering-0B1F4D) |
| **Векторное хранилище** | ![FAISS](https://img.shields.io/badge/FAISS-0467DF?logo=meta&logoColor=white) ![Qdrant](https://img.shields.io/badge/Qdrant-DC244C) ![Chroma](https://img.shields.io/badge/Chroma-FF6446) |
| **Дообучение и оценка** | ![LoRA](https://img.shields.io/badge/LoRA-orange) ![RAGAS](https://img.shields.io/badge/RAGAS-success) |
| **Сервис и инфраструктура** | ![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white) ![Linux](https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black) |
| **Разработка и данные** | ![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white) ![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white) ![arXiv](https://img.shields.io/badge/arXiv-B31B1B?logo=arxiv&logoColor=white) |

<img src="docs/img/divider.svg" alt="" width="100%">

## 📅 План работы

> Приблизительный план на учебный год — этапы и сроки будут уточняться вместе с куратором.

| Этап | Период | Что делаем | Результат |
|:----:|:------:|------------|-----------|
| **1** | Октябрь | **Постановка задачи.** Выбор домена и корпуса, согласование метрик | Описание проекта, репозиторий |
| **2** | Ноябрь | **Корпус документов.** Сбор, очистка, разбиение на чанки | Подготовленный корпус |
| **3** | Декабрь | **Индексация.** Выбор модели эмбеддингов, построение векторного индекса | Проиндексированный корпус |
| **4** | Январь – февраль | **Retrieval + генерация.** Поиск фрагментов и генерация ответа LLM | Baseline RAG |
| **5** | Февраль – март | **Оценка.** Тестовый набор вопросов с эталонами (в т.ч. adversarial), первые замеры | Размеченный набор, отчёт с метриками |
| **6** | Март – апрель | **Улучшения.** Настройка retrieval, борьба с галлюцинациями, LoRA, сравнение RAG vs fine-tuning | Сравнительный анализ |
| **7** | Май | **Анализ ошибок.** Разбор неудачных ответов и меры по их снижению | Разбор failure cases |
| **8** | Июнь | **Финал.** Итоговая документация, демо, защита | Готовый проект |

### Чек-лист

- [x] Создан репозиторий проекта
- [ ] Определены домен и корпус документов
- [ ] Корпус собран и проиндексирован
- [ ] Реализован baseline RAG
- [ ] Собран тестовый набор вопросов с эталонами
- [ ] Проведена оценка качества
- [ ] Выполнено сравнение RAG vs fine-tuning
- [ ] Задокументированы неудачные ответы и меры по их снижению
- [ ] Подготовлена защита проекта

<img src="docs/img/divider.svg" alt="" width="100%">

## 📊 Метрики

> Набор метрик и целевые значения предварительные — пороги будут согласованы с куратором.

| Метрика | Что показывает | Ориентир |
|---------|----------------|:--------:|
| **Faithfulness** | ответ опирается на найденные источники, без выдумок | ≈ 0.8+ |
| **Answer relevance** | ответ действительно отвечает на вопрос | ≈ 0.8+ |
| **Context precision / recall** | насколько релевантны и полны найденные фрагменты | ≈ 0.7+ |
| **Human eval** | экспертная оценка ответов | ≈ 4 / 5 |
| **Latency** | время отклика системы | ≈ до 5 с |

**Критерии приёмки (предварительно)**

1. Корпус документов собран и проиндексирован.
2. Ответы на тестовом наборе вопросов оценены по релевантности и достоверности **выше согласованного порога**.
3. Задокументированы случаи неудачных ответов и предложены меры их снижения.

<img src="docs/img/divider.svg" alt="" width="100%">

## 📁 Структура репозитория

> 🚧 _Раздел в разработке_

## 🚀 Запуск

> 🚧 _Раздел в разработке_

<img src="docs/img/divider.svg" alt="" width="100%">

<div align="center">

<img src="docs/img/footer.svg" alt="RAG-система / дообучение LLM под домен" width="100%">

</div>
