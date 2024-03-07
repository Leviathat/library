from typing import Optional, List

from models.book import BookBase, BookIn, BookOut
from repositories.books import BookRepository


class BookService:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    async def get_books(self) -> List[BookOut]:
        return await self.repository.get_books()

    async def create_book(self, book: BookIn) -> BookOut:
        created_book = await self.repository.create_book(book)
        return created_book

    async def get_book(self, book_id: int) -> Optional[BookOut]:
        return await self.repository.get_book(book_id)

    async def update_book(self, book_id: int, book: BookIn) -> Optional[BookOut]:
        return await self.repository.update_book(book_id, book)

    async def delete_book(self, book_id: int) -> None:
        await self.repository.delete_book(book_id)
