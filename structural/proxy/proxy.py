"""
O Proxy é um padrão de projeto estrutural que tem a
intenção de fornecer um objeto substituto que atua
como se fosse o objeto real que o código cliente
gostaria de usar.
O proxy receberá as solicitações e terá controle
sobre como e quando repassar tais solicitações ao
objeto real.

Com base no modo como o proxies são usados,
nós os classificamos como:

- Proxy Virtual: controla acesso a recursos que podem
ser caros para criação ou utilização.
- Proxy Remoto: controla acesso a recursos que estão
em servidores remotos.
- Proxy de proteção: controla acesso a recursos que
possam necessitar autenticação ou permissão.
- Proxy inteligente: além de controlar acesso ao
objeto real, também executa tarefas adicionais para
saber quando e como executar determinadas ações.

Proxies podem fazer várias coisas diferentes:
criar logs, autenticar usuários, distribuir serviços,
criar cache, criar e destruir objetos, adiar execuções
e muito mais...
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from time import sleep


class IUser(ABC):
    firstname: str
    lastname: str

    @abstractmethod
    def get_addresses(self) -> list[dict]: ...

    @abstractmethod
    def get_user_data(self) -> dict: ...


class User(IUser):
    def __init__(self, firstname: str, lastname: str) -> None:
        sleep(2)  # Simulando requisição
        self.firstname = firstname
        self.lastname = lastname

    def get_addresses(self) -> list[dict]:
        sleep(2)
        return [{'rua': 'Av. Brasil', 'numero': 500}]

    def get_user_data(self) -> dict:
        sleep(2)
        return {'cpf': '123.123.123.12', 'rg': 'CD111111111'}


class UserProxy(IUser):
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname

        self._real_user: User

        self._cached_addresses: list[dict]
        self._all_user_data: dict

    def get_user(self) -> None:
        if not hasattr(self, '_real_user'):
            self._real_user = User(self.firstname, self.lastname)

    def get_addresses(self) -> list[dict]:
        self.get_user()

        if not hasattr(self, '_cached_addresses'):
            self._cached_addresses = self._real_user.get_addresses()

        return self._cached_addresses

    def get_user_data(self) -> dict:
        self.get_user()

        if not hasattr(self, '_all_user_data'):
            self._all_user_data = self._real_user.get_user_data()

        return self._all_user_data


if __name__ == '__main__':
    vini = UserProxy('Vini', 'Sant')

    print(vini.get_user_data())
    print(vini.get_addresses())

    # Cache no proxy - resposta rápida:
    print('Cached:')
    for i in range(50):
        print(vini.get_addresses())
