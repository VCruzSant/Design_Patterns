"""
Na programação POO, o termo factory (fábrica) refere-se a uma classe ou método
que é responsável por criar objetos.

Vantagens:
    Permitem criar um sistema com baixo acoplamento entre classes porque
    ocultam as classes que criam os objetos do código cliente.

    Facilitam a adição de novas classes ao código, porque o cliente não
    conhece e nem utiliza a implementação da classe (utiliza a factory).

    Podem facilitar o processo de "cache" ou criação de "singletons" porque a
    fábrica pode retornar um objeto já criado para o cliente, ao invés de criar
    novos objetos sempre que o cliente precisar.

Desvantagens:
    Podem introduzir muitas classes no código

Vamos ver 2 tipos de Factory da GoF: Factory method e Abstract Factory

Nessa aula:
Simple Factory <- Uma espécie de Factory Method parametrizado
Simple Factory pode não ser considerado um padrão de projeto por si só
Simple Factory pode quebrar princípios do SOLID
"""
from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def search_client(self) -> str | None:
        ...


class VehicleLuxury(Vehicle):
    def search_client(self) -> str | None:
        print('Carro de luxo está buscando cliente...')


class VehiclePopular(Vehicle):
    def search_client(self) -> str | None:
        print('Carro popular está buscando cliente...')


class Moto(Vehicle):
    def search_client(self) -> str | None:
        print('Moto está buscando cliente...')


class VehicleFactory:
    def __init__(self, type_):
        self.car = self.get_vehicle(type_)

    @staticmethod
    def get_vehicle(type_: str) -> Vehicle | None:
        if type_ == 'luxury':
            return VehicleLuxury()
        if type_ == 'popular':
            return VehiclePopular()
        if type_ == 'moto':
            return Moto()

        assert 0, 'Vehicle not exists'

    def search_client(self):
        self.car.search_client()  # type: ignore


if __name__ == "__main__":
    from random import choice
    car_available = ['luxury', 'popular', 'moto']

    for i in range(10):
        car = VehicleFactory(choice(car_available))
        car.search_client()  # type: ignore
