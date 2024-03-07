from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Factory
from fastapi import Depends

from repositories import books
from services.books import BookService


class Container(DeclarativeContainer):
    wiring_config = {
        # Replace with the actual implementation of your repository
        "repositories.book_repository": Factory(books.BookRepository),
        "services.item_service": Factory(
            BookService,
            repositories=Depends(providers="repositories.book_repository"),
        ),
    }
