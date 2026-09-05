from dataclasses import dataclass


@dataclass(frozen=True)
class Book:
    id: int
    title: str

    def __post_init__(self):
        if type(self.id) is not int or self.id <= 0:
            raise ValueError("Book ID must be a positive integer")
        if not isinstance(self.title, str) or not self.title.strip():
            raise ValueError("Title cannot be blank")


@dataclass(frozen=True)
class Review:
    book_id: int
    rating: int

    def __post_init__(self):
        if type(self.book_id) is not int or self.book_id <= 0:
            raise ValueError("Book ID must be a positive integer")
        if type(self.rating) is not int or not 1 <= self.rating <= 5:
            raise ValueError("Rating must be an integer from 1 to 5")
