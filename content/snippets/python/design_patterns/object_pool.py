class PooledObject:
    def __init__(self):
        self.value = None

class ObjectPool:
    def __init__(self):
        self._pool = []
    def acquire(self):
        return self._pool.pop() if self._pool else PooledObject()
    def release(self, obj):
        self._pool.append(obj)

if __name__ == '__main__':
    p = ObjectPool()
    o = p.acquire()
    o.value = 1
    print(o.value)
    p.release(o)
