class ThresholdDiscount:
    def apply(self, price: int) -> int:
        return price - 100 if price >= 1000 else price


if __name__ == "__main__":
    for price in [999, 1000, 1200]:
        print(ThresholdDiscount().apply(price))
