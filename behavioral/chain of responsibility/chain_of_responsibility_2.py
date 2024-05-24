from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self) -> None:
        self.successor: Handler

    @abstractmethod
    def handle(self, letter: str) -> str: ...


class HandlerABC(Handler):
    def __init__(self, successor: Handler) -> None:
        self.letters: list[str] = ['A', 'B', 'C']
        self.successor = successor

    def handle(self, letter: str) -> str:
        if letter in self.letters:
            return f'ABC: tratei {letter}'

        return self.successor.handle(letter)


class HandlerDEF(Handler):
    def __init__(self, successor: Handler) -> None:
        self.letters: list[str] = ['D', 'E', 'F']
        self.successor = successor

    def handle(self, letter: str) -> str:
        if letter in self.letters:
            return f'DEF: tratei {letter}'

        return self.successor.handle(letter)


class HandlerUnsolved(Handler):
    def handle(self, letter: str) -> str:
        return f'Unsolved: Não consigo tratar {letter}'


if __name__ == '__main__':
    handler_unsolved = HandlerUnsolved()
    handler_def = HandlerDEF(handler_unsolved)
    handler_abc = HandlerABC(handler_def)

    print(handler_abc.handle('A'))
    print(handler_abc.handle('C'))
    print(handler_abc.handle('D'))
    print(handler_abc.handle('V'))
