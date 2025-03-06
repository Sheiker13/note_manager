# Note Manager

## Описание проекта
**Note Manager** – это веб-приложение для ведения заметок с возможностью управления пользователями и ролевой моделью доступа. Оно предоставляет RESTful API для работы с заметками, аутентификацию пользователей и веб-интерфейс на Django Templates.

## Основные возможности
- Регистрация и аутентификация пользователей
- Управление заметками (создание, редактирование, удаление, просмотр)
- Разграничение доступа (пользователь, администратор)
- Поддержка Django Templates для веб-интерфейса
- REST API с CRUD-операциями (Django REST Framework)
- Возможность асинхронных задач с Celery (по желанию)
- Использование базы данных SQLite (по умолчанию)

## Технологии
- Python 3
- Django
- Django REST Framework
- SQLite (или PostgreSQL)
- Celery (опционально)
- Docker (опционально)

## Установка и запуск

### 1. Клонирование репозитория
```sh
    git clone <[https://github.com/Sheiker13/note_manager]>
    cd note-manager
```

### 2. Создание и активация виртуального окружения
```sh
    python -m venv venv
    source venv/bin/activate  # Для Linux/Mac
    venv\Scripts\activate  # Для Windows
```

### 3. Установка зависимостей
```sh
    pip install django djangorestframework django-cors-headers
```

### 4. Применение миграций и запуск сервера
```sh
    python manage.py migrate
    python manage.py runserver
```

Сервер будет доступен по адресу: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Использование API
API доступно по адресу `/api/` и включает:
- `GET /api/notes/` – список заметок
- `POST /api/notes/` – создание заметки
- `GET /api/notes/{id}/` – просмотр заметки
- `PUT /api/notes/{id}/` – обновление заметки
- `DELETE /api/notes/{id}/` – удаление заметки

## Запуск с помощью Docker (опционально)
```sh
    docker-compose up --build
```
