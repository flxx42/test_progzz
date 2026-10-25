# FastAPI: учебное демо 

Главный файл — `bookzz.py`. В


## Подготовка

```bash
python3 -m venv demoenv
source demoenv/bin/activate
python -m pip install -r requirements.txt
```

## Запуск

```bash
python -m uvicorn app:app --reload
```

После запуска:

- приложение: http://127.0.0.1:8000
- Получить список все книги: GET http://127.0.0.1:8000/books
- Получить книгу с ID 1: GET http://127.0.0.1:8000/books/1
 
- добавить книгу Открой в браузере:
        http://127.0.0.1:8000/add-book — форма для добавления книги.

- Удалить книгу с ID 3: 

curl -X 'DELETE' \
  'http://127.0.0.1:8000/books/3' \
  -H 'accept: */*'
  
- документация: http://127.0.0.1:8000/docs

## Проверка по мере реализации

```bash
curl http://127.0.0.1:8000/
curl http://127.0.0.1:8000/health
curl "http://127.0.0.1:8000/hello?name=Anna"
```

Перед последним шагом задайте настройки и перезапустите сервер:

```bash
через файл .env
см пример:
.env.example 


Проверка:

```bash
curl http://127.0.0.1:8000/info
```

## Если нужно быстро восстановить правильный вариант

```bash
cp rez_copy_bookzz.py bookzz.py
```



