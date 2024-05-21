def singleton(class_):
    instances = {}

    def get_class(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return get_class


@singleton
class AppSettings:
    def __init__(self) -> None:
        print('OI')
        self.them = 'Light'


if __name__ == "__main__":
    as1 = AppSettings()
    as1.them = 'Dark'
    print(as1.them)

    as2 = AppSettings()
    print(as2.them)
    # o Them voltará ser Light -> Problema de __init__ + singleton

    print(as1)
    print(as2)
