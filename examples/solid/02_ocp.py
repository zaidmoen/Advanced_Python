"""OCP: extend discount behavior without editing checkout."""
from typing import Protocol


def checkout_before(price: int, kind: str) -> int:
    if kind == "regular":
        return price
    if kind == "student":
        return price * 90 // 100
    raise ValueError("Unknown discount")


class Discount(Protocol):
    def apply(self, price: int) -> int: ...


class NoDiscount:
    def apply(self, price: int) -> int:
        return price


class StudentDiscount:
    def apply(self, price: int) -> int:
        return price * 90 // 100


class FixedDiscount:
    def apply(self, price: int) -> int:
        return max(0, price - 200)


def checkout(price: int, discount: Discount) -> int:
    """Price is a non-negative integer in cents."""
    if type(price) is not int or price < 0:
        raise ValueError("Price must be non-negative integer cents")
    return discount.apply(price)


if __name__ == "__main__":
    print(checkout_before(1000, "student"))
    for policy in [NoDiscount(), StudentDiscount(), FixedDiscount()]:
        print(checkout(1000, policy))  # 1000, 900, 800
