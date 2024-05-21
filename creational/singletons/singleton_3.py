# class Meta(type):
#     def __call__(cls, *args, **kwargs):
#         print('CALL DA META EXEC')
#         return super().__call__(*args, **kwargs)


# class People(metaclass=Meta):
#     def __new__(cls, *args, **kwargs):
#         print('NEW EXEC')
#         return super().__new__(cls)

#     def __init__(self, name):
#         print('INIT EXEC')
#         self.name = name

#     def __call__(self):
#         print('CALL EXEC')
#         print('Call chamado')


# if __name__ == '__main__':
#     p1 = People('Vini')
#     p1()
#     print(p1.name)

class Singleton(type):
    _instances: dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__()

        return cls._instances[cls]


class AppSettings(metaclass=Singleton):
    def __init__(self) -> None:
        self.them = 'Light'


if __name__ == '__main__':
    as1 = AppSettings()
    as1.them = 'Dark'

    as2 = AppSettings()
    print(as2.them)
