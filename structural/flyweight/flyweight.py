"""
Flyweight é um padrão de projeto estrutural
que tem a intenção de usar compartilhamento
para suportar eficientemente grandes quantidades
de objetos de forma granular.

Só use o Flyweight quanto TODAS as condições
a seguir forem verdadeiras:

- uma aplicação utiliza uma grande quantidade de
objetos;
- os custos de armazenamento são altos por causa
da grande quantidade de objetos;
- a maioria dos estados de objetos podem se tornar
extrínsecos;
- muitos objetos podem ser substituídos por poucos
objetos compartilhados;
- a aplicação não depende da identidade dos objetos.

Importante:
- Estado intrínseco é o estado do objeto que não muda,
esse estado deve estar dentro do objeto flyweight;
- Estado extrínseco é o estado do objeto que muda,
esse estado pode ser movido para fora do objeto
flyweight;

Dicionário:
Intrínseco - que faz parte de ou que constitui a
essência, a natureza de algo; que é próprio de
algo; inerente.
Extrínseco - que não pertence à essência de algo;
que é exterior.
"""

from __future__ import annotations
# from abc import ABC, abstractmethod


class Client:
    def __init__(self, name) -> None:
        self.name = name
        self.addresses: list = []

        # Extrinsic address data
        self.address_number: str
        self.address_details: str

    def add_address(self, address: Address) -> None:
        self.addresses.append(address)

    def list_addresses(self) -> None:
        for address in self.addresses:
            address.show_address(self.address_number, self.address_details)


class Address:
    """ Flyweight """

    def __init__(self, street: str, neighborhood: str, zipcode: str) -> None:
        self._street = street
        self._neighborhood = neighborhood
        self._zipcode = zipcode

    def show_address(self, address_number: str, address_details: str) -> None:
        print(
            self._street, address_number, address_details
        )


class AddressFactory:
    _addresses: dict = {}

    def _get_key(self, **kwargs):
        return ''.join(kwargs.values())

    def get_address(self, **kwargs) -> Address:
        key = self._get_key(**kwargs)

        try:
            address_flyweight = self._addresses[key]
            print('Usando objeto já criado')
        except KeyError:
            address_flyweight = Address(**kwargs)
            self._addresses[key] = address_flyweight
            print('Criando novo obj')

        return address_flyweight


if __name__ == '__main__':
    address_factory = AddressFactory()

    a1 = address_factory.get_address(
        street='Av Brasil',
        neighborhood='Center',
        zipcode='01234-567'
    )

    a2 = address_factory.get_address(
        street='Av Brasil',
        neighborhood='Center',
        zipcode='01234-567'
    )

    vini = Client('Vini')
    vini.address_number = '50'
    vini.address_details = 'Home'
    vini.add_address(a1)
    vini.list_addresses()

    sant = Client('sant')
    sant.address_number = '250A'
    sant.address_details = 'Home'
    sant.add_address(a1)
    sant.list_addresses()

    print(a1 == a2)
