"""Class, instance state, shared class attribute, and self."""

class Student:
    school = "An-Najah"

    def __init__(self, name: str):
        self.name = name
        self.skills: list[str] = []

    def learn(self, skill: str) -> None:
        self.skills.append(skill)

    def describe(self) -> str:
        return f"{self.name}: {self.skills} at {self.school}"


if __name__ == "__main__":
    zaid = Student("Zaid")
    sara = Student("Sara")
    zaid.learn("Python")
    print(zaid.describe())
    print(sara.describe())  # Independent list: []
