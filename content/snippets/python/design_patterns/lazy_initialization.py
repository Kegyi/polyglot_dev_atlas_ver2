class LazySingleton:
    _instance = None
    def __init__(self):
        self.value = 0
    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = LazySingleton()
        return cls._instance

if __name__ == '__main__':
    LazySingleton.instance().value = 9
    print(LazySingleton.instance().value)
