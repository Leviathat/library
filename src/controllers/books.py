from fastapi import APIRouter, Depends, HTTPException
from services import books
from models.book import BookOut
from typing import List


router = APIRouter()


@router.get("/books", response_model=List[BookOut])
def get_books(book_service: books.BookService = Depends()):
    books = book_service.get_books()
    return books
