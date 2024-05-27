"""
Mediator é um padrão de projeto comportamental
que tem a intenção de definir um objeto que
encapsula a forma como um conjunto de objetos
interage. O Mediator promove o baixo acoplamento
ao evitar que os objetos se refiram uns aos
outros explicitamente e permite variar suas
interações independentemente.
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Colleague(ABC):
    def __init__(self) -> None:
        self.name: str

    @abstractmethod
    def broadcast(self, msg: str) -> None: ...

    @abstractmethod
    def direct(self, msg: str) -> None: ...


class Person(Colleague):
    def __init__(self, name: str, madiator: Mediator) -> None:
        self.name = name
        self.mediator = madiator

    def broadcast(self, msg: str) -> None:
        self.mediator.broadcast(self, msg)

    def send_direct(self, receiver: str, msg) -> None:
        self.mediator.direct(self, receiver, msg)

    def direct(self, msg: str) -> None:
        print(msg)


class Mediator(ABC):
    @abstractmethod
    def broadcast(self, colleague: Colleague, msg: str) -> None: ...

    @abstractmethod
    def direct(self, sender: Colleague,
               receiver: str, msg: str) -> None: ...


class Chatroom(Mediator):
    def __init__(self) -> None:
        self.colleagues: list[Colleague] = []

    def is_colleague(self, colleague: Colleague) -> bool:
        return colleague in self.colleagues

    def add(self, colleague: Colleague) -> None:
        if not self.is_colleague(colleague):
            self.colleagues.append(colleague)

    def remove(self, colleague: Colleague) -> None:
        if self.is_colleague(colleague):
            self.colleagues.remove(colleague)

    def broadcast(self, colleague: Colleague, msg: str) -> None:
        if not self.is_colleague(colleague):
            return
        print(f'{colleague.name} say: {msg}')

    def direct(self, sender: Colleague, receiver: str, msg: str) -> None:
        if not self.is_colleague(sender):
            return

        receiver_obj: list[Colleague] = [
            c for c in self.colleagues
            if c.name == receiver
        ]

        if not receiver_obj:
            return

        receiver_obj[0].direct(
            f'{sender.name} for {receiver_obj[0].name}: {msg}'
        )


if __name__ == '__main__':
    chat = Chatroom()

    roberto = Person('Roberto', chat)
    clara = Person('Clara', chat)
    maria = Person('Maria', chat)
    lorenzo = Person('Lorenzo', chat)

    chat.add(roberto)
    chat.add(clara)
    chat.add(maria)
    chat.add(lorenzo)

    roberto.broadcast('Hi People!')
    clara.broadcast('Hi!')

    print()
    roberto.send_direct('Clara', 'Hi Clara')
