"""Composition with duck typing (no shared parent required)."""
from typing import Protocol


class Sender(Protocol):
    def send(self, message: str) -> None: ...


class ConsoleSender:
    def send(self, message: str) -> None:
        print(message)


class WelcomeService:
    def __init__(self, sender: Sender):
        self.sender = sender

    def welcome(self, name: str) -> None:
        self.sender.send(f"Welcome, {name}!")


if __name__ == "__main__":
    WelcomeService(ConsoleSender()).welcome("Zaid")
