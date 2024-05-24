"""
Chain of responsibility (COR) é um padrão comportamental
que tem a intenção de evitar o acoplamento do remetente de
uma solicitação ao seu receptor, ao dar a mais de um objeto
a oportunidade de tratar a solicitação.
Encadear os objetos receptores passando a solicitação
ao longo da cadeia até que um objeto a trate.
"""


def handler_ABC(letter: str) -> str:
    letters = ['A', 'B', 'C']

    if letter in letters:
        return f'ABC: Tratei o valor {letter}'

    return handler_DEF(letter)


def handler_DEF(letter: str) -> str:
    letters = ['D', 'E', 'F']

    if letter in letters:
        return f'DEF: Tratei o valor {letter}'

    return handler_unsolved(letter)


def handler_unsolved(letter: str) -> str:
    return f'unsolved: não sei tratar {letter}'


if __name__ == '__main__':
    print(handler_ABC('A'))
    print(handler_ABC('B'))
    print(handler_ABC('C'))
    print(handler_ABC('D'))
