from fastapi import FastAPI,status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

books = [
  {
    "id": 1,
    "title": "The Pragmatic Programmer",
    "author": "Andrew Hunt, David Thomas",
    "publisher": "Addison-Wesley",
    "published_date": "1999-10-20",
    "page_count": 352,
    "language": "English"
  },
  {
    "id": 2,
    "title": "Clean Code",
    "author": "Robert C. Martin",
    "publisher": "Prentice Hall",
    "published_date": "2008-08-11",
    "page_count": 464,
    "language": "English"
  },
  {
    "id": 3,
    "title": "Introduction to the Theory of Computation",
    "author": "Michael Sipser",
    "publisher": "Cengage Learning",
    "published_date": "2012-06-27",
    "page_count": 504,
    "language": "English"
  },
  {
    "id": 4,
    "title": "Artificial Intelligence: A Modern Approach",
    "author": "Stuart Russell, Peter Norvig",
    "publisher": "Pearson",
    "published_date": "2020-04-28",
    "page_count": 1136,
    "language": "English"
  },
  {
    "id": 5,
    "title": "Deep Learning",
    "author": "Ian Goodfellow, Yoshua Bengio, Aaron Courville",
    "publisher": "MIT Press",
    "published_date": "2016-11-18",
    "page_count": 800,
    "language": "English"
  }
]

class BookModel(BaseModel):
  id: int
  title: str
  author: str
  publisher: str
  published_date: str
  page_count: int
  language: str
  
class BookUpdateModel(BaseModel):
  title: str
  author: str
  publisher: str
  page_count: int
  language: str

@app.get("/books", response_model=List[BookModel])
async def get_all_books():
  return books

@app.post("/books",status_code=status.HTTP_201_CREATED)
async def create_book(book: BookModel)->dict:
  new_book = book.model_dump()
  books.append(new_book)
  return new_book

@app.get("/books/{book_id}")
async def get_book(book_id: int)->dict:
  for book in books:
    if book["id"] == book_id:
      return book
    
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@app.patch("/books/{book_id}")
async def update_book(book_id: int, update_book: BookUpdateModel)->dict:
  for book in books:
    if book["id"] == book_id:
      book["title"] = update_book.title
      book["author"] = update_book.author
      book["publisher"] = update_book.publisher
      book["page_count"] = update_book.page_count
      book["language"] = update_book.language
      return book
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    

@app.delete("/books/{book_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
  for book in books:
    if book["id"] == book_id:
      books.remove(book)
      return {"message": "Book deleted successfully"}
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")