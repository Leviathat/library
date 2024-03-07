from typing import Optional, List

from models.book import BookIn, BookOut


class BookRepository:

    async def create_book(self, book: BookIn) -> BookOut:
        # Implement logic to create a book in the database
        raise NotImplementedError

    async def get_book(self, book_id: int) -> Optional[BookOut]:
        # Implement logic to fetch a book from the database by ID
        raise NotImplementedError

    async def update_book(self, book_id: int, book: BookIn) -> Optional[BookOut]:
        # Implement logic to update a book in the database
        raise NotImplementedError

    async def delete_book(self, book_id: int) -> None:
        # Implement logic to delete a book from the database
        raise NotImplementedError

    async def get_books(self) -> List[BookOut]:
        # Implement logic to fetch all books from the database
        raise NotImplementedError
