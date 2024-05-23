"""
O Padrão de projeto State é um padrão comportamental
que tem a intenção de permitir a um objeto mudar
seu comportamento quando o seu estado interno
muda.
O objeto parecerá ter mudado sua classe.
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class OrderState(ABC):
    def __init__(self, order: Order) -> None:
        self.order = order

    @abstractmethod
    def pending(self) -> None: ...

    @abstractmethod
    def approve(self) -> None: ...

    @abstractmethod
    def reject(self) -> None: ...

    def __str__(self) -> str:
        return self.__class__.__name__


class PaymentPending(OrderState):
    def pending(self) -> None:
        print('Pagamento Já pendente, não posso fazer nada')

    def approve(self) -> None:
        self.order.state = PaymentAproved(self.order)
        print('Pagamento aprovado')

    def reject(self) -> None:
        self.order.state = PaymentRejected(self.order)
        print('Pagamento recusado')


class PaymentAproved(OrderState):
    def pending(self) -> None:
        self.order.state = PaymentPending(self.order)
        print('Pagamento pendente')

    def approve(self) -> None:
        print('Pagamento Já aprovado, não posso fazer nada')

    def reject(self) -> None:
        self.order.state = PaymentRejected(self.order)
        print('Pagamento recusado')


class PaymentRejected(OrderState):
    def pending(self) -> None:
        print('Pagamento recusado, não vou mover para pendente')

    def approve(self) -> None:
        print('Pagamento recusado, não vou mover para aprovado')

    def reject(self) -> None:
        print('Pagamento já está recusado')


class Order:
    """ Context """

    def __init__(self) -> None:
        self.state: OrderState = PaymentPending(self)

    def pending(self) -> None:
        print('Trying exec pending()')
        self.state.pending()
        print(f'Estado atual: {self.state}')
        print()

    def approve(self) -> None:
        print('Trying exec approve()')
        self.state.approve()
        print(f'Estado atual: {self.state}')
        print()

    def reject(self) -> None:
        print('Trying exec reject()')
        self.state.reject()
        print(f'Estado atual: {self.state}')
        print()


if __name__ == '__main__':
    order = Order()
    order.pending()
    order.approve()
    order.pending()
    order.reject()
    order.pending()
    order.approve()
