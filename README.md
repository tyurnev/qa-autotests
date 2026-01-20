# QA Autotests (January)

Проект с базовыми автотестами на Python и pytest.
Используется для отработки структуры проекта, модулей и unit-тестов.

## Требования

- Python 3.10+
- macOS / Linux (Windows аналогично)

## Установка и запуск

### 1. Клонировать репозиторий

```bash
git clone <repo_url>
cd qa-autotests-2026
```

### 2. Создать виртуальное окружение

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Установить зависимости

```bash
pip install -r requirements.txt
```

### 4. Запустить тесты

```bash
pytest
```

## Структура проекта

```text
src/app/         — исходный код (модули)
tests/unit/      — unit-тесты
pytest.ini       — конфигурация pytest
requirements.txt — зависимости проекта
```

## Примечания

- Тесты запускаются одной командой `pytest` из корня проекта
- Виртуальное окружение `venv` не коммитится в репозиторий
