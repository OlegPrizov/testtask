# testtask

### как запустить бэкенд
1. Создать и активировать виртуальное окружение: 
```python3 -m venv venv```
```source venv/bin/activate```
2. Установить зависимости: ```pip install -r requirements.txt```
4. Перейти в директорию backend ```cd backend/```
5. Применить миграции: ```python manage.py migrate```
8. Запустить сервер: ```python manage.py runserver```