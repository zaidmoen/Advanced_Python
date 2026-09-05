from collections.abc import Iterable
from .models import Book, Review


class MemoryBookRepository:
    def __init__(self, books: Iterable[Book] = ()):
        self._books: dict[int, Book] = {}
        for book in books:
            if book.id in self._books:
                raise ValueError("Duplicate book ID")
            self._books[book.id] = book

    def get(self, book_id: int) -> Book | None:
        return self._books.get(book_id)


class MemoryReviewRepository:
    def __init__(self):
        self._reviews: list[Review] = []

    def add(self, review: Review) -> None:
        self._reviews.append(review)

    def for_book(self, book_id: int) -> list[Review]:
        return [review for review in self._reviews if review.book_id == book_id]
