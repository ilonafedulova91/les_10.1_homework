# Banking Operations Widget

## Описание проекта
Проект представляет собой бэкенд‑часть виджета для личного кабинета клиента банка. Виджет отображает несколько последних *успешных банковских операций* клиента.

В рамках проекта реализованы функции для:

-маскировки номеров банковских карт и счетов

-форматирования дат

-фильтрации и сортировки операций

Проект развивается пошагово в рамках домашних заданий курса.

## Цель проекта
Подготовка и обработка банковских данных для безопасного и удобного отображения в пользовательском интерфейсе:

-защита чувствительных данных (карты, счета)

-удобная работа с датами

-фильтрация и сортировка операций

## Структура проекта

project_root/

├── src/

│ ├── masks.py

│ ├── widget.py

│ └── processing.py

├── tests/

├── .flake8

├── pyproject.toml

├── .gitignore

└── README.md

## Установка и настройка
### 1. Клонирование репозитория
git clone <URL_репозитория>


### 2. Установка зависимостей
Проект использует **Poetry**.

poetry install --with lint
### 3. Инструменты качества кода
В группу lint входят:

-**flake8** — проверка стиля

-**black** — форматирование

-**isort** — сортировка импортов

-**mypy** — проверка типов

Запуск:

poetry run flake8 src

poetry run black src

poetry run isort src

poetry run mypy src

## Реализованные модули и функции

### masks

**get_mask_card_number(card_number: str) -> str**

Маскирует номер банковской карты.

Пример:

get_mask_card_number("7000792289606361")

7000 79** **** 6361

**get_mask_account(account_number: str) -> str**

Маскирует номер банковского счета.

Пример:

get_mask_account("73654108430135874305")

**4305

### widget

**mask_account_card(data: str) -> str**

Определяет тип данных (карта или счёт) и возвращает замаскированный номер.

Примеры:

mask_account_card("Visa Platinum 7000792289606361")

Visa Platinum 7000 79** **** 6361

mask_account_card("Счет 73654108430135874305")

Счет **4305

**get_date(date_str: str) -> str**

Преобразует дату из ISO‑формата в формат ДД.ММ.ГГГГ.

Пример:

get_date("2024-03-11T02:26:18.671407")

11.03.2024

### processing

**filter_by_state(data: list[dict], state: str = 'EXECUTED') -> list[dict]**

Фильтрует операции по статусу.

Пример:

filter_by_state(operations)

filter_by_state(operations, 'CANCELED')

**sort_by_date(data: list[dict], reverse: bool = True) -> list[dict]**

Сортирует операции по дате.

Пример:

sort_by_date(operations)

sort_by_date(operations, reverse=False)

## Git и GitHub

-Репозиторий инициализирован с помощью git init

-Используется .gitignore для Python

-Работа ведётся по GitFlow (ветки feature / develop / main)

-Проект размещён на GitHub

## Статус проекта

Проект находится в активной разработке и будет дополняться в следующих заданиях курса.
