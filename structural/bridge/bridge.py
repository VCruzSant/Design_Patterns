"""
Bridge é um padrão de projeto estrutural que
tem a intenção de desacoplar uma abstração
da sua implementação, de modo que as duas
possam variar e evoluir independentemente.

Abstração é uma camada de alto nível para algo.
Geralmente, a abstração não faz nenhum trabalho
por conta própria, ela delega parte ou todo o
trabalho para a camada de implementação.

RELEMBRANDO: Adapter é um padrão de projeto
estrutural que tem a intenção de permitir
que duas classes que seriam incompatíveis
trabalhem em conjunto através de um "adaptador".

Diferença (GOF pag. 208) - A diferença chave
entre esses padrões está nas suas intenções...
...O padrão Adapter faz as coisas funcionarem
APÓS elas terem sido projetadas; o Bridge as
faz funcionar ANTES QUE existam...
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class IRemoteControl(ABC):
    @abstractmethod
    def increase_volume(self) -> None: ...

    @abstractmethod
    def decrease_volume(self) -> None: ...

    @abstractmethod
    def power(self) -> None: ...


class RemoteControl(IRemoteControl):
    def __init__(self, device: IDevice) -> None:
        self._device = device

    def increase_volume(self) -> None:
        self._device.volume += 10

    def decrease_volume(self) -> None:
        self._device.volume -= 10

    def power(self) -> None:
        self._device.power = not self._device.power


class IDevice(ABC):
    @property
    @abstractmethod
    def volume(self) -> int: ...

    @volume.setter
    def volume(self, volume: int) -> None: ...

    @property
    @abstractmethod
    def power(self) -> bool: ...

    @power.setter
    def power(self, power: bool) -> None: ...


class TV(IDevice):
    def __init__(self) -> None:
        self._volume = 10
        self._power = False
        self._name = self.__class__.__name__

    @property
    def volume(self) -> int:
        return self._volume

    @volume.setter
    def volume(self, volume: int) -> None:
        if not self._power:
            return print(f'Turn {self._name} on')

        elif volume > 100:
            return

        elif volume < 0:
            return

        self._volume = volume
        print(f'Volume: {self._volume}')

    @property
    def power(self) -> bool:
        return self._power

    @power.setter
    def power(self, power: bool) -> None:
        self._power = power
        power_status = 'ON' if self._power else 'OFF'
        return print(f'{self.__class__.__name__} {power_status}')


if __name__ == "__main__":
    tv = TV()

    remote_control = RemoteControl(tv)
    remote_control.decrease_volume()
    remote_control.decrease_volume()
    remote_control.power()
    remote_control.decrease_volume()
    remote_control.decrease_volume()
    remote_control.increase_volume()
    remote_control.increase_volume()
    remote_control.power()
    remote_control.increase_volume()
    remote_control.power()
