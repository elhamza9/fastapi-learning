from fastapi import FastAPI

app = FastAPI()

@app.get("/hello/{name}")
async def hello(name: str):
    return {'message': f'Hello {name} !'}


@app.get("/square/{nbr}")
async def square(nbr: int):
    return {'message': f'Square of {nbr} is {nbr**2} !'}


BOOKS = [
        {"name": "Calculus", "cat": "math"},
        {"name": "Algebra", "cat": "math"},
        {"name": "WWI", "cat": "history"},
        {"name": "WW2", "cat": "history"},
        {"name": "Weather of Africa", "cat": "geography"},
]

@app.get("/books/")
async def get_books(cat: str):
    books_to_return = []
    for book in BOOKS:
        if book["cat"].casefold() == cat.casefold():
            books_to_return.append(book)
    return books_to_return

