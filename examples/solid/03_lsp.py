"""LSP: do not promise flying for every bird."""
from abc import ABC, abstractmethod


class BirdBefore:
    def fly(self) -> str:
        return "Flying"


class PenguinBefore(BirdBefore):
    def fly(self) -> str:
        raise NotImplementedError("Penguins cannot fly")


class FlyingBird(ABC):
    @abstractmethod
    def fly(self) -> str:
        """Return a description of successful flight."""


class Sparrow(FlyingBird):
    def fly(self) -> str:
        return "Sparrow flying"


class Penguin:
    def swim(self) -> str:
        return "Penguin swimming"


def launch(bird: FlyingBird) -> str:
    return bird.fly()


if __name__ == "__main__":
    try:
        PenguinBefore().fly()
    except NotImplementedError as error:
        print(f"Broken contract: {error}")
    print(launch(Sparrow()))
    print(Penguin().swim())
