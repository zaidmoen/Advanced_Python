from typing import Protocol
from .models import Book, Review


class BookReader(Protocol):
    def get(self, book_id: int) -> Book | None:
        """Return a book, or None when absent."""
        ...


class ReviewWriter(Protocol):
    def add(self, review: Review) -> None:
        """Store one review."""
        ...


class ReviewReader(Protocol):
    def for_book(self, book_id: int) -> list[Review]:
        """Return all reviews for the book as an independent list."""
        ...
