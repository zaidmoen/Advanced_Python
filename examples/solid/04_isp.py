"""ISP: a read-only client should not require write capability."""
from typing import Protocol


class ReadWriteBefore(Protocol):
    def read(self) -> str: ...
    def write(self, value: str) -> None: ...


class ReadOnlyBefore:
    def read(self) -> str:
        return "Python notes"

    def write(self, value: str) -> None:
        raise NotImplementedError("Read-only source")


class Reader(Protocol):
    def read(self) -> str: ...


class Writer(Protocol):
    def write(self, value: str) -> None: ...


class ReadOnlyNotes:
    def read(self) -> str:
        return "Python notes"


def display_before(source: ReadWriteBefore) -> str:
    return source.read()  # This client never needed write().


def display(source: Reader) -> str:
    return source.read()


if __name__ == "__main__":
    print(display_before(ReadOnlyBefore()))
    print(display(ReadOnlyNotes()))
