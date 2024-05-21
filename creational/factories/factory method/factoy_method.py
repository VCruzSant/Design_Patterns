"""
Factory method é um padrão de criação que permite definir uma interface para
criar objetos, mas deixa as subclasses decidirem quais objetos criar. O
Factory method permite adiar a instanciação para as subclasses, garantindo o
baixo acoplamento entre classes.
"""

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def search_client(self) -> str | None: ...


class VehicleLuxury(Vehicle):
    def search_client(self) -> str | None:
        print('Carro de luxo está buscando cliente...')


class VehiclePopular(Vehicle):
    def search_client(self) -> str | None:
        print('Carro popular está buscando cliente...')


class Moto(Vehicle):
    def search_client(self) -> str | None:
        print('Moto está buscando cliente...')


class VehicleFactory(ABC):
    def __init__(self, type_):
        self.car = self.get_vehicle(type_)

    @staticmethod
    @abstractmethod
    def get_vehicle(type_: str) -> Vehicle | None: ...

    def search_client(self):
        self.car.search_client()  # type: ignore


class NorthZoneVehicleFactory(VehicleFactory):
    @staticmethod
    def get_vehicle(type_: str) -> Vehicle | None:
        if type_ == 'luxury':
            return VehicleLuxury()
        if type_ == 'popular':
            return VehiclePopular()
        if type_ == 'moto':
            return Moto()

        assert 0, 'Vehicle not exists'


class SouthZoneVehicleFactory(VehicleFactory):
    @staticmethod
    def get_vehicle(type_: str) -> Vehicle | None:
        if type_ == 'popular':
            return VehiclePopular()

        assert 0, 'Vehicle not exists'


if __name__ == "__main__":
    from random import choice
    vehicle_available_north_zone = ['luxury', 'popular', 'moto']
    vehicle_available_south_zone = ['popular']

    print('NORTH ZONE')
    for i in range(10):
        car = NorthZoneVehicleFactory(choice(vehicle_available_north_zone))
        car.search_client()  # type: ignore
    print()

    print('SOUTH ZONE')
    for i in range(10):
        car2 = SouthZoneVehicleFactory(choice(vehicle_available_south_zone))
        car2.search_client()  # type: ignore
    print()
