from abc import ABC, abstractmethod


class Pizza(ABC):
    def prepare(self) -> None:
        """template method"""
        self.hook_before_ingredients()
        self.add_ingredients()
        self.hook_after_ingredients()
        self.cook()
        self.cut()
        self.serve()

    def hook_before_ingredients(self) -> None: ...
    def hook_after_ingredients(self) -> None: ...

    def cut(self) -> None:
        print(f'{self.__class__.__name__}: Cutting pizza')

    def serve(self) -> None:
        print(f'{self.__class__.__name__}: Serving pizza')

    @abstractmethod
    def add_ingredients(self) -> None: ...

    @abstractmethod
    def cook(self) -> None: ...


class Cheese(Pizza):
    def add_ingredients(self) -> None:
        print(f'{self.__class__.__name__}: Add Cheeses')

    def cook(self) -> None:
        print(f'{self.__class__.__name__}: Cooking in 45 minutes')


class Veg(Pizza):
    def hook_before_ingredients(self) -> None:
        print(f'{self.__class__.__name__}: Washing ingredients')

    def add_ingredients(self) -> None:
        print(f'{self.__class__.__name__}: Add salad')

    def cook(self) -> None:
        print(f'{self.__class__.__name__}: Cooking in 25 minutes')


if __name__ == '__main__':
    cheese_pizza = Cheese()
    cheese_pizza.prepare()
    print()

    veg_pizza = Veg()
    veg_pizza.prepare()
