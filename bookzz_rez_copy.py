import os

from fastapi import FastAPI, HTTPException, Form, status
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Наш первый сервис")

@app.get("/")
def root():
    return {"message": "Сервис работает"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/hello")
def hello(name: str = "студент"):
    return {"message": f"Привет, {name}!"}


books = [
    {"id": 1, "title": "1984", "author": "George Orwell", "year": 1949},
    {"id": 2, "title": "Brave New World", "author": "Aldous Huxley", "year": 1932},
]
next_id = 3


@app.get("/books")
def get_books():
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Книга не найдена")


# Эндпоинт для отображения HTML-формы
@app.get("/add-book")
def show_add_book_form():
    html = """
    <!DOCTYPE html>
    <html>
      <head><title>Добавить книгу</title></head>
      <body>
        <h2>Добавить книгу</h2>
        <form action="/books" method="post">
          <label>Название: <input type="text" name="title" required></label><br><br>
          <label>Автор: <input type="text" name="author" required></label><br><br>
          <label>Год издания: <input type="number" name="year"></label><br><br>
          <button type="submit">Добавить</button>
        </form>
        <p><a href="/books">Вернуться к каталогу</a></p>
      </body>
    </html>
    """
    return HTMLResponse(content=html)


# Приём данных из формы (multipart/form-data)
@app.post("/books", status_code=status.HTTP_201_CREATED)
def add_book(
    title: str = Form(...),
    author: str = Form(...),
    year: int | None = Form(None),
):
    if not title or not author:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Поля title и author обязательны"
        )

    global next_id
    new_book = {
        "id": next_id,
        "title": title,
        "author": author,
        "year": year,
    }
    next_id += 1
    books.append(new_book)
    return new_book


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    global books
    original_len = len(books)
    books = [b for b in books if b["id"] != book_id]

    if len(books) == original_len:
        raise HTTPException(status_code=404, detail="Книга не найдена")
        

@app.get("/info")
def info():
    app_name = os.getenv("APP_NAME", "Учебный сервис")
    app_author = os.getenv("APP_AUTHOR", "Не указан")

    return {
        "app_name": app_name,
        "author": app_author,
    }
