class Adaptee:
    def specific(self): print('Adaptee specific')
class Target:
    def request(self): raise NotImplementedError
class ClassAdapter(Adaptee, Target):
    def request(self): self.specific()

if __name__ == '__main__':
    ClassAdapter().request()
