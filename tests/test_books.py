import unittest
from book_project.models import Book, Review
from book_project.repositories import MemoryBookRepository, MemoryReviewRepository
from book_project.services import RatingService, ReviewService
from solutions.policy_service import ReviewService as PolicyService, HighRatingPolicy, StandardPolicy


class BookTests(unittest.TestCase):
    def setUp(self):
        self.books = MemoryBookRepository([Book(1, 'Python'), Book(2, 'SQL')])
        self.reviews = MemoryReviewRepository()
        self.service = ReviewService(self.books, self.reviews)

    def test_review_and_average(self):
        self.service.add_review(1, 5)
        self.service.add_review(1, 3)
        self.service.add_review(2, 1)
        self.assertEqual(RatingService(self.reviews).average(1), 4.0)

    def test_missing_book_does_not_write(self):
        with self.assertRaises(LookupError):
            self.service.add_review(99, 5)
        self.assertEqual(self.reviews.for_book(99), [])

    def test_invalid_ratings_do_not_write(self):
        for value in [0, 6, True, 3.5, '5', None]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                self.service.add_review(1, value)
        self.assertEqual(self.reviews.for_book(1), [])

    def test_empty_average(self):
        self.assertIsNone(RatingService(self.reviews).average(1))

    def test_query_result_is_independent(self):
        self.service.add_review(1, 5)
        result = self.reviews.for_book(1)
        result.clear()
        self.assertEqual(len(self.reviews.for_book(1)), 1)

    def test_repositories_do_not_share_state(self):
        self.service.add_review(1, 5)
        self.assertEqual(MemoryReviewRepository().for_book(1), [])

    def test_book_validation(self):
        for book_id, title in [(0, 'A'), (True, 'A'), (1, ''), (1, '  ')]:
            with self.subTest(book_id=book_id, title=title), self.assertRaises(ValueError):
                Book(book_id, title)

    def test_duplicate_book_id(self):
        with self.assertRaises(ValueError):
            MemoryBookRepository([Book(1, 'A'), Book(1, 'B')])

    def test_missing_book_contract(self):
        self.assertIsNone(self.books.get(99))

    def test_service_accepts_independent_implementations(self):
        class Catalog:
            def get(self, book_id):
                return Book(7, 'Testing') if book_id == 7 else None
        class Sink:
            def __init__(self):
                self.saved = []
            def add(self, review):
                self.saved.append(review)
        sink = Sink()
        ReviewService(Catalog(), sink).add_review(7, 4)
        self.assertEqual(sink.saved, [Review(7, 4)])

    def test_injected_policy_accepts_or_rejects_before_writing(self):
        for policy, accepted in [(StandardPolicy(), True), (HighRatingPolicy(), False)]:
            with self.subTest(policy=type(policy).__name__):
                reviews = MemoryReviewRepository()
                service = PolicyService(self.books, reviews, policy)
                if accepted:
                    service.add_review(1, 2)
                else:
                    with self.assertRaises(ValueError):
                        service.add_review(1, 2)
                self.assertEqual(len(reviews.for_book(1)), int(accepted))


if __name__ == '__main__':
    unittest.main()
