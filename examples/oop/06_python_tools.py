"""Dataclasses, alternate constructors, static methods, equality."""
from dataclasses import dataclass, field


@dataclass
class Book:
    title: str
    tags: list[str] = field(default_factory=list)

    @classmethod
    def from_text(cls, text: str) -> "Book":
        return cls(title=text.strip())

    @staticmethod
    def is_valid_title(title: str) -> bool:
        return bool(title.strip())

    def __str__(self) -> str:
        return self.title


if __name__ == "__main__":
    first = Book.from_text(" Python ")
    second = Book("Python")
    print(first == second, first is second)  # True False
    first.tags.append("OOP")
    print(second.tags)  # []
    print(str(first), repr(first))
    print(Book.is_valid_title(" "))  # False; validation is not automatic.
