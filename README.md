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

<div align="center">

<table>
  <tr>
    <td align="center" width="340">
      <br/>
      <img src="https://img.shields.io/badge/%D0%9A%D1%83%D1%80%D0%B0%D1%82%D0%BE%D1%80-0F2D69?style=for-the-badge" alt="Куратор" />
      <br/><br/>
      <b><i>ФИО куратора</i></b>
      <br/>
      <sub>Руководитель проекта</sub>
      <br/><br/>
    </td>
    <td align="center" width="340">
      <br/>
      <img src="https://img.shields.io/badge/%D0%A1%D1%82%D1%83%D0%B4%D0%B5%D0%BD%D1%82-1E50C8?style=for-the-badge" alt="Студент" />
      <br/><br/>
      <b><i>ФИО</i></b>
      <br/>
      <sub>Исполнитель проекта</sub>
      <br/><br/>
      <a href="https://github.com/ArmbristerVlad"><img src="https://img.shields.io/badge/@ArmbristerVlad-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub @ArmbristerVlad" /></a>
      <br/><br/>
    </td>
  </tr>
</table>

</div>

<!-- TODO: указать ФИО куратора и своё -->

<img src="docs/img/divider.svg" alt="" width="100%">

## 🧰 Планируемый стек

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
