from .contracts import BookReader, ReviewReader, ReviewWriter
from .models import Review


class ReviewService:
    def __init__(self, books: BookReader, reviews: ReviewWriter):
        self._books = books
        self._reviews = reviews

    def add_review(self, book_id: int, rating: int) -> Review:
        review = Review(book_id, rating)
        if self._books.get(book_id) is None:
            raise LookupError("Book not found")
        self._reviews.add(review)
        return review


class RatingService:
    def __init__(self, reviews: ReviewReader):
        self._reviews = reviews

    def average(self, book_id: int) -> float | None:
        reviews = self._reviews.for_book(book_id)
        if not reviews:
            return None
        return sum(review.rating for review in reviews) / len(reviews)
