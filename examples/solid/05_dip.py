"""DIP: business logic depends on a contract; wire details outside."""
from typing import Protocol


class MemoryReader:
    def read(self) -> str:
        return "OOP and SOLID"


class ReportServiceBefore:
    def __init__(self):
        self.reader = MemoryReader()  # Hard-wired implementation.

    def report(self) -> str:
        return self.reader.read().upper()


class Reader(Protocol):
    def read(self) -> str: ...


class ReportService:
    def __init__(self, reader: Reader):
        self.reader = reader

    def report(self) -> str:
        return self.reader.read().upper()


class FakeReader:
    def read(self) -> str:
        return "test data"


if __name__ == "__main__":
    print(ReportServiceBefore().report())
    print(ReportService(MemoryReader()).report())
    print(ReportService(FakeReader()).report())
