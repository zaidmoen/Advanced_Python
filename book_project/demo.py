from .models import Book
from .repositories import MemoryBookRepository, MemoryReviewRepository
from .services import RatingService, ReviewService


def main() -> None:
    books = MemoryBookRepository([Book(1, "Python Practice")])
    reviews = MemoryReviewRepository()
    service = ReviewService(books, reviews)
    service.add_review(1, 5)
    service.add_review(1, 3)
    print(f"Average rating: {RatingService(reviews).average(1)}")
    try:
        service.add_review(99, 4)
    except LookupError as error:
        print(error)


if __name__ == "__main__":
    main()
