"""
Template Method (comportamental) tem a intenção de definir
um algoritmo em um método, postergando alguns passos
para as subclasses por herança. Template method permite
que subclasses redefinam certos passos de um algoritmo
sem mudar a estrutura do mesmo.

Também é possível definir hooks para que as subclasses
utilizem caso necessário.

The Hollywood principle: "Don't Call Us, We'll Call You."
(IoC - Inversão de controle)
"""
from abc import ABC, abstractmethod


class Abstract(ABC):
    def template_method(self):
        self.hook()
        self.operation1()
        self.operation2()
        self.base_class_method()
        print()

    def hook(self): ...

    def base_class_method(self):
        print('Im from Class Abstract')

    @abstractmethod
    def operation1(self): ...

    @abstractmethod
    def operation2(self): ...


class ConcreteClass(Abstract):
    def hook(self):
        print('Im hook')

    def operation1(self):
        print('Operation 1 OK')

    def operation2(self):
        print('Operation 2 OK')


class ConcreteClass2(Abstract):
    def operation1(self):
        print('Operation 1 OK (diferent)')

    def operation2(self):
        print('Operation 2 OK (diferent)')


if __name__ == "__main__":
    c1 = ConcreteClass()
    c1.template_method()

    c2 = ConcreteClass2()
    c2.template_method()
