"""
Abstract Factory é um padrão de criação que fornece uma interface para criar
famílias de objetos relacionados ou dependentes sem especificar suas classes
concretas. Geralmente Abstract Factory conta com um ou mais Factory Methods
para criar seus objetos.

Uma diferença importante entre Factory Method e Abstract Factory é que o
Factory Method usa herança, enquanto Abstract Factory usa a composição.

Princípio: programe para interfaces, não para implementações
"""

from abc import ABC, abstractmethod


class VehicleLuxury(ABC):
    @abstractmethod
    def search_custommer(self) -> str | None: ...


class VehiclePopular(ABC):
    @abstractmethod
    def search_custommer(self) -> str | None: ...


class CarLuxuryNZ(VehicleLuxury):
    def search_custommer(self) -> str | None:
        print('Carro de luxo NZ está buscando cliente...')


class CarPopularNZ(VehiclePopular):
    def search_custommer(self) -> str | None:
        print('Carro NZ popular está buscando cliente...')


class MotoNZ(VehiclePopular):
    def search_custommer(self) -> str | None:
        print('Moto está NZ buscando cliente...')


class CarLuxurySZ(VehicleLuxury):
    def search_custommer(self) -> str | None:
        print('Carro de luxo SZ está buscando cliente...')


class CarPopularSZ(VehiclePopular):
    def search_custommer(self) -> str | None:
        print('Carro popular SZ está buscando cliente...')


class MotoSZ(VehiclePopular):
    def search_custommer(self) -> str | None:
        print('Moto SZ está buscando cliente...')


class VehicleFactory(ABC):
    @staticmethod
    @abstractmethod
    def get_vehicle_luxury() -> VehicleLuxury | None: ...

    @staticmethod
    @abstractmethod
    def get_vehicle_popular() -> VehiclePopular | None: ...

    @staticmethod
    @abstractmethod
    def get_moto_popular() -> VehiclePopular | None: ...


class NorthZoneVehicleFactory(VehicleFactory):
    @staticmethod
    def get_vehicle_luxury() -> VehicleLuxury | None:
        return CarLuxuryNZ()

    @staticmethod
    def get_vehicle_popular() -> VehiclePopular | None:
        return CarPopularNZ()

    @staticmethod
    def get_moto_popular() -> VehiclePopular | None:
        return MotoNZ()


class SouthZoneVehicleFactory(VehicleFactory):
    @staticmethod
    def get_vehicle_luxury() -> VehicleLuxury | None:
        return CarLuxurySZ()

    @staticmethod
    def get_vehicle_popular() -> VehiclePopular | None:
        return CarPopularSZ()

    @staticmethod
    def get_moto_popular() -> VehiclePopular | None:
        return MotoSZ()


class Custommer:
    def search_custommers(self):
        for factory in [NorthZoneVehicleFactory(), SouthZoneVehicleFactory()]:
            car_popular = factory.get_vehicle_popular()
            car_popular.search_custommer()

            car_luxury = factory.get_vehicle_luxury()
            car_luxury.search_custommer()

            moto_popular = factory.get_moto_popular()
            moto_popular.search_custommer()


if __name__ == "__main__":
    custommer = Custommer()
    custommer.search_custommers()
