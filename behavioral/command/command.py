"""
Command tem intenção de encapsular uma solicitação como
um objeto, desta forma permitindo parametrizar clientes com diferentes
solicitações, enfileirar ou fazer registro (log) de solicitações e suportar
operações que podem ser desfeitas.

É formado por um cliente (quem orquestra tudo), um invoker (que invoca as
solicitações), um ou vários objetos de comando (que fazem a ligação entre o
receiver e a ação a ser executada) e um receiver (o objeto que vai executar a
ação no final).
"""
from abc import ABC, abstractmethod


class Light:
    """ Receiver - Smart Light"""

    def __init__(self, name: str, room_name: str) -> None:
        self.name = name
        self.room_name = room_name
        self.color = 'Default color'

    def on(self) -> None:
        print(f'{self.name} in {self.room_name} is now ON')

    def off(self) -> None:
        print(f'{self.name} in {self.room_name} is now OFF')

    def change_color(self, color):
        self.color = color
        print(f'{self.name} in {self.room_name} is now {self.color}')


class ICommand(ABC):
    """ Command Interface"""
    @abstractmethod
    def execute(self) -> None: ...

    @abstractmethod
    def undo(self) -> None: ...


class LightCommand(ICommand):
    """ Concrete Command """

    def __init__(self, light: Light) -> None:
        self.light = light

    def execute(self) -> None:
        self.light.on()

    def undo(self) -> None:
        self.light.off()


class LightChangeColor(ICommand):
    """ Concrete Command """

    def __init__(self, light: Light, color: str) -> None:
        self.light = light
        self.color = color
        self._old_color = self.light.color

    def execute(self) -> None:
        self._old_color = self.light.color
        self.light.change_color(self.color)

    def undo(self) -> None:
        self.light.change_color(self._old_color)


class RemoteController:
    """ Controller """

    def __init__(self) -> None:
        self._buttons: dict[str, ICommand] = {}
        self._undos: list[tuple[str, str]] = []

    def add_command(self, id_: str, command: ICommand) -> None:
        self._buttons[id_] = command

    def button_execute(self, id_: str) -> None:
        if id_ in self._buttons:
            self._buttons[id_].execute()
            self._undos.append((id_, 'execute'))

    def button_execute_again(self, id_: str) -> None:
        if id_ in self._buttons:
            self._buttons[id_].undo()
            self._undos.append((id_, 'undo'))

    def global_undo(self):
        if not self._undos:
            return None

        # pegando ultimos da lista
        button_name, action = self._undos[-1]

        if action == 'execute':
            self._buttons[button_name].undo()
        else:
            self._buttons[button_name].execute()

        # remove a ultima ação
        self._undos.pop()


if __name__ == "__main__":
    bedroom_light = Light('light', 'bedroom')
    bedroom_light_on = LightCommand(bedroom_light)
    bedroom_light_blue = LightChangeColor(bedroom_light, 'Blue')
    bedroom_light_red = LightChangeColor(bedroom_light, 'Red')

    controller = RemoteController()
    controller.add_command('Light Bedroom', bedroom_light_on)
    controller.add_command('Bedroom Color Blue', bedroom_light_blue)
    controller.add_command('Bedroom Color Red', bedroom_light_red)

    controller.button_execute('Light Bedroom')
    controller.button_execute_again('Light Bedroom')
    controller.button_execute('Bedroom Color Blue')
    # controller.button_execute_again('Bedroom Color Blue')
    controller.button_execute('Bedroom Color Red')
    controller.button_execute_again('Bedroom Color Red')
    print()

    controller.global_undo()
    controller.global_undo()
    controller.global_undo()
    controller.global_undo()
    controller.global_undo()
