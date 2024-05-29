"""
Composite é um padrão de projeto estrutural que permite que
você utilize a composição para criar objetos em estruturas
de árvores. O padrão permite aos clientes tratarem de maneira
uniforme objetos individuais (Leaf) e composições de
objetos (Composite).

IMPORTANTE: só aplique este padrão em uma estrutura que possa
ser representada em formato hierárquico (árvore).

No padrão composite, temos dois tipos de objetos:
Composite (que representa nós internos da árvore) e Leaf
(que representa nós externos da árvore).

Objetos Composite são objetos mais complexos e com filhos.
Geralmente, eles delegam trabalho para os filhos usando
um método em comum.
Objetos Leaf são objetos simples, da ponta e sem filhos.
Geralmente, são esses objetos que realizam o trabalho
real da aplicação.
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class BoxStructure(ABC):
    """ Component """
    @abstractmethod
    def print_content(self) -> None: ...

    @abstractmethod
    def get_price(self) -> float: ...

    def add(self, child: BoxStructure) -> None: ...
    def remove(self, child: BoxStructure) -> None: ...


class Box(BoxStructure):
    """ Composit """

    def __init__(self, name) -> None:
        self.name = name
        self._children: list[BoxStructure] = []

    def print_content(self) -> None:
        for child in self._children:
            child.print_content()

    def get_price(self) -> float:
        return sum([
            child.get_price() for child in self._children
        ])

    def add(self, child: BoxStructure) -> None:
        self._children.append(child)

    def remove(self, child: BoxStructure) -> None:
        if child in self._children:
            self._children.remove(child)


class Product(BoxStructure):
    def __init__(self, name: str, price: int) -> None:
        self.name = name
        self.price = price

    def print_content(self) -> None:
        print(self.name, self.price)

    def get_price(self) -> float:
        return self.price


if __name__ == '__main__':
    # leaf
    tshirt1 = Product('tshirt', 50)
    tshirt2 = Product('tshirt', 60)
    tshirt3 = Product('tshirt', 70)

    # composite
    box_tshirt = Box('Box of tshirt')

    box_tshirt.add(tshirt1)
    box_tshirt.add(tshirt2)
    box_tshirt.add(tshirt3)

    box_tshirt.print_content()
    print(box_tshirt.get_price())
    print()

    # leaf
    smartphone1 = Product('smartphone1', 5000)
    smartphone2 = Product('smartphone2', 17000)

    # composite
    box_smartphone = Box('Box of smartphone')
    box_smartphone.add(smartphone1)
    box_smartphone.add(smartphone2)
    box_smartphone.print_content()

    # Composite
    big_box = Box('BIG box')
    big_box.add(box_tshirt)
    big_box.add(box_smartphone)
    big_box.print_content()
    print(big_box.get_price())
