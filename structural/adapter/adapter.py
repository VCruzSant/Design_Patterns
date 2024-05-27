"""
Adapter é um padrão de projeto estrutural que
tem a intenção de permitir que duas classes
que seriam incompatíveis trabalhem em conjunto
através de um "adaptador".
"""

from abc import ABC, abstractmethod


class IControl(ABC):
    @abstractmethod
    def top(self) -> None: ...

    @abstractmethod
    def right(self) -> None: ...

    @abstractmethod
    def down(self) -> None: ...

    @abstractmethod
    def left(self) -> None: ...


class Control(IControl):
    def top(self) -> None:
        print('Moving top')

    def right(self) -> None:
        print('Moving right')

    def down(self) -> None:
        print('Moving down')

    def left(self) -> None:
        print('Moving left')

# Exemplo: contrato uma empresa que tem controles de melhores plataformas
# mas fazer a mesma coisa
# Preciso adaptar meu controle ao controle da nova empresa


class NewControl:
    def move_top(self) -> None:
        print('NewControl Moving top')

    def move_right(self) -> None:
        print('NewControl Moving right')

    def move_down(self) -> None:
        print('NewControl Moving down')

    def move_left(self) -> None:
        print('NewControl Moving left')


class ControlAdapter:
    def __init__(self, new_control: NewControl) -> None:
        self.new_control = new_control

    def top(self) -> None:
        self.new_control.move_top()

    def right(self) -> None:
        self.new_control.move_right()

    def down(self) -> None:
        self.new_control.move_down()

    def left(self) -> None:
        self.new_control.move_left()


class ControlAdapter2(Control, NewControl):
    def top(self) -> None:
        self.move_top()

    def right(self) -> None:
        self.move_right()

    def down(self) -> None:
        self.move_down()

    def left(self) -> None:
        self.move_left()


if __name__ == '__main__':
    new_control = NewControl()
    c1 = ControlAdapter(new_control)
    c2 = ControlAdapter2()

    c1.top()
    c1.right()
    c1.down()
    c1.left()

    print()

    c2.top()
    c2.right()
    c2.down()
    c2.left()
