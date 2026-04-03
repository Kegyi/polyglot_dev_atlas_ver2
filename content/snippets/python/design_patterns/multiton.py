class Multiton:
    _instances = {}
    def __init__(self, key):
        self.key = key
    @classmethod
    def get(cls, key):
        if key not in cls._instances:
            cls._instances[key] = Multiton(key)
        return cls._instances[key]

if __name__ == '__main__':
    a = Multiton.get('a')
    b = Multiton.get('b')
    print(a.key, b.key)
