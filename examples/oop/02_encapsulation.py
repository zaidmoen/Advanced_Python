"""A read-only property and methods protect an account invariant."""

class BankAccount:
    def __init__(self):
        self._balance = 0  # Integer cents, not floating-point money.

    @property
    def balance(self) -> int:
        return self._balance

    @staticmethod
    def _validate_amount(amount: int) -> None:
        if type(amount) is not int or amount <= 0:
            raise ValueError("Amount must be a positive integer number of cents")

    def deposit(self, amount: int) -> None:
        self._validate_amount(amount)
        self._balance += amount

    def withdraw(self, amount: int) -> None:
        self._validate_amount(amount)
        if amount > self._balance:
            raise ValueError("Insufficient balance")
        self._balance -= amount


if __name__ == "__main__":
    account = BankAccount()
    account.deposit(1000)
    account.withdraw(300)
    print(account.balance)  # 700
    try:
        account.withdraw(800)
    except ValueError as error:
        print(error)
    print(account.balance)  # Still 700
