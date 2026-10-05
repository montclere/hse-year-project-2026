<!-- ================= HEADER ================= -->
<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&height=170&color=0:0B1F4D,50:1E50C8,100:4C8DF6&section=header" alt="" />

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Inconsolata&weight=600&size=34&duration=3500&pause=600&color=4C8DF6&center=true&vCenter=true&repeat=true&width=900&height=100&lines=RAG-%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0+%2F+%D0%B4%D0%BE%D0%BE%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5+LLM+%D0%BF%D0%BE%D0%B4+%D0%B4%D0%BE%D0%BC%D0%B5%D0%BD+%F0%9F%94%8E;%D0%A2%D0%BE%D1%87%D0%BD%D1%8B%D0%B5+%D0%BE%D1%82%D0%B2%D0%B5%D1%82%D1%8B+%D0%BF%D0%BE+%D0%B1%D0%BE%D0%BB%D1%8C%D1%88%D0%BE%D0%BC%D1%83+%D0%BA%D0%BE%D1%80%D0%BF%D1%83%D1%81%D1%83+%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%BE%D0%B2;Retrieval+%C2%B7+Generation+%C2%B7+Evaluation;%D0%9C%D0%B5%D0%BD%D1%8C%D1%88%D0%B5+%D0%B3%D0%B0%D0%BB%D0%BB%D1%8E%D1%86%D0%B8%D0%BD%D0%B0%D1%86%D0%B8%D0%B9+%E2%80%94+%D0%B1%D0%BE%D0%BB%D1%8C%D1%88%D0%B5+%D1%84%D0%B0%D0%BA%D1%82%D0%BE%D0%B2" alt="RAG-система / дообучение LLM под домен" />

<br/>

![Status](https://img.shields.io/badge/status-in_progress-4C8DF6?style=flat-square)
![Level](https://img.shields.io/badge/level-PRO-1E50C8?style=flat-square)
![Task](https://img.shields.io/badge/task-QA_%2B_text_generation-0F2D69?style=flat-square)
![Year](https://img.shields.io/badge/годовой_проект-2026%E2%80%932027-0B1F4D?style=flat-square)

</div>

<!-- ================= ABOUT ================= -->
<img width="100%" src="https://capsule-render.vercel.app/api?type=rect&height=2&color=0:0B1F4D,50:1E50C8,100:4C8DF6&section=header" alt="" />

## 🎯 О проекте

Система вопрос-ответ по корпусу документов на основе **RAG** (Retrieval-Augmented Generation) или дообученной LLM — с оценкой качества ответов и разбором случаев галлюцинаций.

> **Проблема.** Пользователям нужны точные ответы по большому корпусу документов. Обычный поиск по ключевым словам не даёт связного ответа, а LLM без контекста «галлюцинирует» — отвечает уверенно, но выдумывает факты.

<div align="center">

| 🔤 Поиск по ключевым словам | 🤖 LLM без контекста | ✅ Наш подход |
|:---:|:---:|:---:|
| находит документы, но не отвечает на вопрос | отвечает связно, но может выдумывать | находит релевантные фрагменты и отвечает **строго по ним** |

</div>

| | |
|---|---|
| 🧩 **Тип задачи** | Question answering, генерация текста |
| 🗂 **Данные** | Собственный корпус документов или открытые корпуса (например, статьи arXiv) |
| 🛠 **Методы** | Эмбеддинги + vector store (FAISS / Qdrant / Chroma) + retrieval + генерация LLM; альтернатива — LoRA fine-tuning небольшой open-source модели |
| 📏 **Метрики** | Human eval, RAGAS (faithfulness, relevance), latency |
| 🧪 **Усложнения** | Сравнение чистого RAG vs fine-tuning; борьба с hallucinations; тест на adversarial-вопросах |
| 🎓 **Уровень** | PRO |

<!-- ================= TEAM ================= -->
<img width="100%" src="https://capsule-render.vercel.app/api?type=rect&height=2&color=0:0B1F4D,50:1E50C8,100:4C8DF6&section=header" alt="" />

## 👥 Команда

### 🧭 Руководители проекта

<div align="center">

| | | | |
|:---:|:---:|:---:|:---:|
| Мовсумов Денис | Абакумов Юрий | Цуриков Виталий | Панчук Георгий |
| Мустафин Фарид | Голубев Александр | Родионов Никита | |

</div>

### 🧑‍🏫 Куратор

> **_ФИО куратора_** <!-- TODO: указать куратора -->

### 🧑‍💻 Участники

| ФИО | Роль | Связь |
|-----|------|-------|
| _ФИО_ | _например, Team Lead / Data_ | [![GitHub](https://img.shields.io/badge/GitHub-4C8DF6?style=flat-square&logo=github&logoColor=white)](https://github.com/) |
| _ФИО_ | _например, Retrieval / Vector store_ | [![GitHub](https://img.shields.io/badge/GitHub-4C8DF6?style=flat-square&logo=github&logoColor=white)](https://github.com/) |
| _ФИО_ | _например, LLM / Generation_ | [![GitHub](https://img.shields.io/badge/GitHub-4C8DF6?style=flat-square&logo=github&logoColor=white)](https://github.com/) |
| _ФИО_ | _например, Evaluation / Testing_ | [![GitHub](https://img.shields.io/badge/GitHub-4C8DF6?style=flat-square&logo=github&logoColor=white)](https://github.com/) |

<!-- TODO: заполнить состав команды -->

<!-- ================= APPROACH ================= -->
<img width="100%" src="https://capsule-render.vercel.app/api?type=rect&height=2&color=0:0B1F4D,50:1E50C8,100:4C8DF6&section=header" alt="" />

## 🧠 Подход

```mermaid
flowchart LR
    A[📄 Корпус] --> B[Чанки]
    B --> C[Эмбеддинги]
    C --> D[(Векторный индекс)]
    Q[❓ Вопрос] --> E[Эмбеддинг запроса]
    E --> F[Top-k retrieval]
    D --> F
    F --> G[Промпт: вопрос + контекст]
    G --> H[🤖 LLM]
    H --> I[✅ Ответ + источники]
```

**RAG vs fine-tuning** — в рамках усложнений сравниваем оба подхода:

| | 🔎 RAG | 🎛 LoRA fine-tuning |
|---|---|---|
| **Знания** | берутся из корпуса в момент запроса | «зашиваются» в веса модели |
| **Обновление корпуса** | переиндексация | повторное обучение |
| **Источники** | можно ссылаться на фрагменты | напрямую не указываются |
| **Риск галлюцинаций** | ниже, если контекст найден верно | выше без опоры на документы |

<!-- ================= STACK ================= -->
<img width="100%" src="https://capsule-render.vercel.app/api?type=rect&height=2&color=0:0B1F4D,50:1E50C8,100:4C8DF6&section=header" alt="" />

## ⚙️ Планируемый стек

<div align="center">

<img src="https://skillicons.dev/icons?i=python,pytorch,fastapi,docker,git,github,linux,postgres&theme=dark&perline=8" alt="Python, PyTorch, FastAPI, Docker, Git, GitHub, Linux, PostgreSQL" />

<br/><br/>

![RAG](https://img.shields.io/badge/RAG-4C8DF6?style=flat-square)
![Embeddings](https://img.shields.io/badge/Embeddings-3A74E8?style=flat-square)
![Vector Search](https://img.shields.io/badge/Vector_Search-1E50C8?style=flat-square)
![Prompt Engineering](https://img.shields.io/badge/Prompt_Engineering-1A44A8?style=flat-square)
![LoRA](https://img.shields.io/badge/LoRA-0F2D69?style=flat-square)
![RAGAS](https://img.shields.io/badge/RAGAS-0B1F4D?style=flat-square)
<br/>
![Hugging Face](https://img.shields.io/badge/Hugging_Face-4C8DF6?style=flat-square&logo=huggingface&logoColor=white)
![FAISS](https://img.shields.io/badge/FAISS-3A74E8?style=flat-square&logo=meta&logoColor=white)
![Qdrant](https://img.shields.io/badge/Qdrant-1E50C8?style=flat-square)
![Chroma](https://img.shields.io/badge/Chroma-1A44A8?style=flat-square)
![Pandas](https://img.shields.io/badge/Pandas-0F2D69?style=flat-square&logo=pandas&logoColor=white)
![arXiv](https://img.shields.io/badge/arXiv-0B1F4D?style=flat-square&logo=arxiv&logoColor=white)

</div>

<!-- ================= PLAN ================= -->
<img width="100%" src="https://capsule-render.vercel.app/api?type=rect&height=2&color=0:0B1F4D,50:1E50C8,100:4C8DF6&section=header" alt="" />

## 🗺 План работы

> Черновой план на учебный год — будет уточняться вместе с куратором. Сроки ориентировочные.

```mermaid
gantt
    title Дорожная карта проекта
    dateFormat  YYYY-MM-DD
    axisFormat  %b
    section Подготовка
    Постановка задачи, выбор домена   :a1, 2026-10-05, 25d
    Сбор и подготовка корпуса         :a2, after a1, 30d
    section Система
    Эмбеддинги и векторный индекс     :b1, after a2, 25d
    Retrieval + генерация (baseline)  :b2, after b1, 35d
    section Оценка
    Тестовый набор вопросов           :c1, after b1, 30d
    Human eval и RAGAS                :c2, after b2, 30d
    section Улучшения
    LoRA, борьба с hallucinations     :d1, after c2, 40d
    Анализ ошибок                     :d2, after d1, 20d
    section Финал
    Документация и защита             :e1, after d2, 25d
```

| | Этап | Результат |
|:-:|------|-----------|
| 1️⃣ | Постановка задачи: домен, корпус, метрики и пороги | Описание проекта, репозиторий |
| 2️⃣ | Сбор, очистка и разбиение корпуса на чанки | Подготовленный корпус |
| 3️⃣ | Эмбеддинги и векторный индекс | Проиндексированный корпус |
| 4️⃣ | Retrieval + генерация ответа LLM | Baseline RAG |
| 5️⃣ | Тестовый набор вопросов с эталонами (в т.ч. adversarial) | Размеченный набор |
| 6️⃣ | Оценка: human eval, RAGAS, latency | Отчёт с метриками |
| 7️⃣ | Улучшения: retrieval, hallucinations, LoRA, RAG vs fine-tuning | Сравнительный анализ |
| 8️⃣ | Анализ неудачных ответов и меры по их снижению | Разбор failure cases |
| 9️⃣ | Итоговая документация, демо, защита | Готовый проект |

<details>
<summary><b>☑️ Чек-лист</b></summary>

<br/>

- [x] Создан репозиторий проекта
- [ ] Определены домен и корпус документов
- [ ] Корпус собран и проиндексирован
- [ ] Реализован baseline RAG
- [ ] Собран тестовый набор вопросов с эталонами
- [ ] Проведена оценка (human eval / RAGAS)
- [ ] Выполнено сравнение RAG vs fine-tuning
- [ ] Задокументированы неудачные ответы и меры по их снижению
- [ ] Подготовлена защита проекта

</details>

<!-- ================= METRICS ================= -->
<img width="100%" src="https://capsule-render.vercel.app/api?type=rect&height=2&color=0:0B1F4D,50:1E50C8,100:4C8DF6&section=header" alt="" />

## 📊 Метрики и критерии приёмки

<div align="center">

| 🎯 Faithfulness | 💬 Relevance | 🧑‍⚖️ Human eval | ⏱ Latency |
|:---:|:---:|:---:|:---:|
| ответ опирается на источники, без выдумок | ответ действительно отвечает на вопрос | экспертная оценка ответов | время отклика системы |

</div>

**Критерии приёмки**

1. Корпус документов собран и проиндексирован.
2. На тестовом наборе вопросов ответы оценены по релевантности и достоверности (human eval или RAGAS) **выше согласованного порога**.
3. Задокументированы случаи неудачных ответов и предложены меры их снижения.

<!-- ================= FOOTER ================= -->
<img width="100%" src="https://capsule-render.vercel.app/api?type=rect&height=2&color=0:0B1F4D,50:1E50C8,100:4C8DF6&section=header" alt="" />

<div align="center">

**RAG-система / дообучение LLM под домен · Годовой проект · Уровень PRO**

</div>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&height=130&color=0:4C8DF6,50:1E50C8,100:0B1F4D&section=footer&reversal=true" alt="" />
