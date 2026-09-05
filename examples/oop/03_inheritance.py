"""Inheritance, overriding, super(), and polymorphism."""

class Employee:
    def __init__(self, name: str):
        self.name = name

    def describe(self) -> str:
        return f"Employee: {self.name}"


class Developer(Employee):
    def __init__(self, name: str, language: str):
        super().__init__(name)
        self.language = language

    def describe(self) -> str:
        return f"{super().describe()} codes in {self.language}"


if __name__ == "__main__":
    for employee in [Employee("Sara"), Developer("Zaid", "Python")]:
        print(employee.describe())
