"""SRP: calculation and presentation change for different reasons."""

class MixedReport:
    def render(self, values: list[int]) -> str:
        return f"TOTAL: {sum(values)}"


class Report:
    def total(self, values: list[int]) -> int:
        return sum(values)


class TextFormatter:
    def format(self, total: int) -> str:
        return f"TOTAL: {total}"


if __name__ == "__main__":
    print(MixedReport().render([10, 20]))
    print(TextFormatter().format(Report().total([10, 20])))
