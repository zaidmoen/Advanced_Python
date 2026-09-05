from typing import Protocol
from book_project.contracts import BookReader, ReviewWriter
from book_project.models import Book, Review
from book_project.repositories import MemoryBookRepository, MemoryReviewRepository


class RatingPolicy(Protocol):
    def validate(self, rating: int) -> None: ...


class StandardPolicy:
    def validate(self, rating: int) -> None:
        if type(rating) is not int or not 1 <= rating <= 5:
            raise ValueError("Expected an integer rating from 1 to 5")


class HighRatingPolicy:
    def validate(self, rating: int) -> None:
        if type(rating) is not int or not 3 <= rating <= 5:
            raise ValueError("This exercise policy accepts ratings from 3 to 5")


class ReviewService:
    def __init__(self, books: BookReader, reviews: ReviewWriter, policy: RatingPolicy):
        self._books = books
        self._reviews = reviews
        self._policy = policy

    def add_review(self, book_id: int, rating: int) -> Review:
        review = Review(book_id, rating)
        self._policy.validate(rating)
        if self._books.get(book_id) is None:
            raise LookupError("Book not found")
        self._reviews.add(review)
        return review


if __name__ == "__main__":
    books = MemoryBookRepository([Book(1, "Python")])
    for policy in [StandardPolicy(), HighRatingPolicy()]:
        reviews = MemoryReviewRepository()
        service = ReviewService(books, reviews, policy)
        try:
            print(service.add_review(1, 2))
        except ValueError as error:
            print(error)
        print(f"Stored: {len(reviews.for_book(1))}")  # 1 then 0
