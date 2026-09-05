from typing import Protocol


class Sender(Protocol):
    def send(self, message: str) -> str: ...


class EmailPreview:
    def send(self, message: str) -> str:
        return f"Email preview: {message}"


class SmsPreview:
    def send(self, message: str) -> str:
        return f"SMS preview: {message}"


class PushPreview:
    def send(self, message: str) -> str:
        return f"Push preview: {message}"


def notify(sender: Sender, message: str) -> str:
    return sender.send(message)


if __name__ == "__main__":
    for sender in [EmailPreview(), SmsPreview(), PushPreview()]:
        print(notify(sender, "Hello"))
