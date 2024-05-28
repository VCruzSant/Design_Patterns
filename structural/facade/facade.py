"""
Façade (Fachada) é um padrão de projeto estrutural
que tem a intenção de fornecer uma interface
unificada para um conjunto de interfaces em um
subsistema. Façade define uma interface de nível
mais alto que torna o subsistema mais fácil de ser
usado.
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class IObservable(ABC):
    @property
    @abstractmethod
    def state(self): ...

    @abstractmethod
    def add_observer(self, observer: IObserver) -> None: ...

    @abstractmethod
    def remove_observer(self, observer: IObserver) -> None: ...

    @abstractmethod
    def notify_observer(self) -> None: ...


class WeatherStation(IObservable):
    """ Observable """

    def __init__(self) -> None:
        self._observers: list[IObserver] = []
        self._state: dict = {}

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state_update: dict) -> None:
        # Dessa maneira consigo identificar chaves existentes, se fornecidas
        new_state: dict = {**self._state, **state_update}

        if new_state != self._state:
            self._state = new_state
            self.notify_observer()

    def reset_state(self):
        self._state = {}

    def add_observer(self, observer: IObserver) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: IObserver) -> None:
        if self._observers:
            self._observers.remove(observer)

    def notify_observer(self) -> None:
        for observer in self._observers:
            observer.update()


class IObserver(ABC):
    @abstractmethod
    def update(self) -> None: ...


class Smartphone(IObserver):
    def __init__(self, name, observable: IObservable) -> None:
        self.name = name
        self.observable = observable

    def update(self) -> None:
        observable_name = self.observable.__class__.__name__
        print(f'{self.name} object {observable_name} has just been updated:'
              f' {self.observable.state}')


class WeatherStationFacade:
    def __init__(self) -> None:
        self.weather_station = WeatherStation()

        self.smartphone = Smartphone('Iphone', self.weather_station)
        self.smartphone_2 = Smartphone('Android', self.weather_station)

        self.weather_station.add_observer(self.smartphone)
        self.weather_station.add_observer(self.smartphone_2)

    def add_observer(self, observer: IObserver) -> None:
        self.weather_station.add_observer(observer)

    def change_state(self, state: dict) -> None:
        self.weather_station.state = state

    def remove_smartphone_1(self) -> None:
        self.weather_station.remove_observer(self.smartphone)

    def remove_smartphone_2(self) -> None:
        self.weather_station.remove_observer(self.smartphone_2)

    def reset_state(self) -> None:
        self.weather_station.reset_state()


if __name__ == "__main__":
    weather_station = WeatherStationFacade()

    weather_station.change_state({'temperature': '26'})
    weather_station.change_state({'temperature': '30'})

    weather_station.remove_smartphone_2()
    weather_station.change_state({'temperature': '26'})
