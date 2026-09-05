class ShoppingCart:
    def __init__(self):
        self._prices: list[int] = []

    def add(self, price: int) -> None:
        if type(price) is not int or price < 0:
            raise ValueError("Price must be non-negative integer cents")
        self._prices.append(price)

    @property
    def total(self) -> int:
        return sum(self._prices)


if __name__ == "__main__":
    first, second = ShoppingCart(), ShoppingCart()
    first.add(100)
    first.add(250)
    print(first.total, second.total)  # 350 0
    try:
        first.add(-1)
    except ValueError as error:
        print(error)
    print(first.total)  # 350
