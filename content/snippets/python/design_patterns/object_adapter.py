class Adaptee:
    def specific(self): print('Adaptee specific')
class Target:
    def request(self): raise NotImplementedError
class ObjectAdapter(Target):
    def __init__(self): self.a = Adaptee()
    def request(self): self.a.specific()

if __name__ == '__main__':
    ObjectAdapter().request()
