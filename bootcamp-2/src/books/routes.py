
from fastapi import APIRouter
from typing import List
from src.books.book_data import books
from src.books.schema import BookModel, BookUpdateModel
from fastapi import HTTPException, status

book_router = APIRouter()

# Get All Books
@book_router.get("/", response_model=List[BookModel])
async def get_all_books():
  return books

# Create a Book
@book_router.post("/",status_code=status.HTTP_201_CREATED)
async def create_book(book: BookModel)->dict:
  new_book = book.model_dump()
  books.book_routerend(new_book)
  return new_book

# Get a Book
@book_router.get("/{book_id}")
async def get_book(book_id: int)->dict:
  for book in books:
    if book["id"] == book_id:
      return book
    
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

# Update a Book
@book_router.patch("/{book_id}")
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
    
# Delete a Book
@book_router.delete("/{book_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
  for book in books:
    if book["id"] == book_id:
      books.remove(book)
      return {"message": "Book deleted successfully"}
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")