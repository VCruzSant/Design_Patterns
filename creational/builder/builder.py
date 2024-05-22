"""
Builder é um padrão de criação que tem a intenção
de separar a construção de um objeto complexo
da sua representação, de modo que o mesmo processo
de construção possa criar diferentes representações.

Builder te da a possibilidade de criar objetos passo-a-passo
e isso já é possível no Python sem este padrão.

Geralmente o builder aceita o encadeamento de métodos
(method chaining).
"""
from abc import ABC, abstractmethod


class StringReprMixin:
    # Caso eu queria printar o a classe instanciada
    # o Retorno vai ser o nome da classe e seus obj:
    def __str__(self):
        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        print(params)
        return f'{self.__class__.__name__}({params})'

    def __repr__(self) -> str:
        return self.__str__()


class User(StringReprMixin):
    def __init__(self) -> None:
        self.firstname = None
        self.lastname = None
        self.age = None
        self.phone_numbers = []
        self.adresses = []


class IUserBuilder(ABC):
    @property
    @abstractmethod
    def result(self): ...

    @abstractmethod
    def add_fisrtname(self, firstname): ...

    @abstractmethod
    def add_lastname(self, lastname): ...

    @abstractmethod
    def add_age(self, age): ...

    @abstractmethod
    def add_phone(self, phone): ...

    @abstractmethod
    def add_address(self, address): ...


class UserBuilder(ABC):
    def __init__(self) -> None:
        self.reset()

    # Utilidade: garantir que sempre vamos trabalhar com User() limpo
    def reset(self):
        self._result = User()

    @property
    def result(self):
        return_data = self._result
        self.reset()
        return return_data

    def add_fisrtname(self, firstname):
        self._result.firstname = firstname
        return self

    def add_lastname(self, lastname):
        self._result.lastname = lastname
        return self

    def add_age(self, age):
        self._result.age = age
        return self

    def add_phone(self, phone):
        self._result.phone_numbers.append(phone)
        return self

    def add_address(self, address):
        self._result.adresses.append(address)
        return self


class UserDirector():
    def __init__(self, builder: UserBuilder) -> None:
        self._builder = builder

    def with_age(self, firstname, lastname, age):
        self._builder.add_fisrtname(firstname)\
            .add_lastname(lastname)\
            .add_age(age)

        return self._builder.result

    def with_address(self, firstname, lastname, address):
        self._builder.add_fisrtname(firstname)\
            .add_lastname(lastname)\
            .add_address(address)

        return self._builder.result

# Posso pular tudo isso usando parâmetros nomeados:
# class User(StringReprMixin):
#     def __init__(
#             self, firstname=None, lastname=None, age=None,
#             phone_numbers=[], adresses=[]
#             ) -> None:
#         self.firstname = firstname
#         self.lastname = lastname
#         self.age = age
#         self.phone_numbers = phone_numbers
#         self.adresses = adresses

#  E depois eu faço getters e setters


if __name__ == "__main__":
    user_builder = UserBuilder()
    user_director = UserDirector(user_builder)
    user1 = user_director.with_age('vini', 'sant', 21)
    user2 = user_director.with_address('vini', 'sant', 'Av Brasil')
    print(user2)
