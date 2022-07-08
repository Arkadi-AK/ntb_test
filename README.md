# Тестовое задание "NTB"

## Установка
```bash
python3 -m venv venv
. venv/bin/activate
cd ntb_test
pip install -r requirements.txt
```

## Запуск

* Выполните миграции # ```python manage.py makemigrations```
* Примените миграции # ```python manage.py migrate```
* Создайте пользователя # ```python manage.py createsuperuser```

Выполните команду, для старта проекта и запуска локального сервера
```python manage.py runserver```