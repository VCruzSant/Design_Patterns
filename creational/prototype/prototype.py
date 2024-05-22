"""
Especificar os tipos de objetos a serem criados
usando uma instância-protótipo e criar novos objetos
pela cópia desse protótipo
"""
from copy import deepcopy


class StringReprMixin:
    # Caso eu queria printar o a classe instanciada
    # o Retorno vai ser o nome da classe e seus obj:
    def __str__(self):
        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'

    def __repr__(self) -> str:
        return self.__str__()


class Address(StringReprMixin):
    def __init__(self, street: str, number: str) -> None:
        self.street = street
        self.number = number


class Person(StringReprMixin):
    def __init__(self, name: str, lastname: str) -> None:
        self.name = name
        self. lastname = lastname
        self.addresses: list = []

    def add_address(self, address: Address) -> None:
        self.addresses.append(address)

    def clone(self):
        return deepcopy(self)


if __name__ == "__main__":

    p1 = Person('Vini', 'Sant')
    address_p1 = Address('av Brasil', '20')
    p1.add_address(address_p1)

    # Exemplo: Se eu quiser adicionar a esposa de p1 e apenas mudar o nome
    # eu não consigo pq ambos vão estar apontados para o mesmo lugar na memória
    # Quando eu for conferir os valores, ambos obj vão estar com o mesmo valor
    # Para solucionar isso, utilizo deepcopy:
    # wife_p1 = deepcopy(p1)

    # Prototype cria um método para isso:
    wife_p1 = p1.clone()
    wife_p1.name = 'Wife'
    print(p1)
    print(wife_p1)
