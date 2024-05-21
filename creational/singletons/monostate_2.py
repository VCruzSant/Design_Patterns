"""
Monostate (ou Borg) - É uma variação do Singleton proposto
por Alex Martelli que tem a intenção de garantir que o
estado do objeto seja igual para todas as instâncias.
"""


class StringReprMixin:
    # Caso eu queria printar o a classe instanciada
    # o Retorno vai ser o nome da classe e seus obj:
    def __str__(self):
        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        print(params)
        return f'{self.__class__.__name__}({params})'

    def __repr__(self) -> str:
        return self.__str__()


class A(StringReprMixin):
    def __init__(self) -> None:
        self.x = 10
        self.y = 5


class MonoState(StringReprMixin):
    _state: dict = {}

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj.__dict__ = cls._state
        return obj

    def __init__(self, name=None, surname=None) -> None:
        # só para o linter o vscode n reclamar
        self.x = 1

        # Com isso, o estado é mantido e todas as instancias tem esse valor
        if name is not None:
            self.name = name

        if surname is not None:
            self.surname = surname


a = A()
print(a)
print()

mono_state_1 = MonoState('Vini', 'Sant')
mono_state_1.x = 678392290
print(mono_state_1)
print()

mono_state_2 = MonoState()
print(mono_state_2)
