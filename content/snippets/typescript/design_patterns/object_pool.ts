class PooledObject { value: number | null = null }
class ObjectPool<T extends PooledObject> {
  private pool: T[] = []
  acquire(factory: () => T) { return this.pool.pop() ?? factory() }
  release(obj: T) { this.pool.push(obj) }
}

const pool = new ObjectPool<PooledObject>()
const o = pool.acquire(() => new PooledObject())
o.value = 7
console.log(o.value)
pool.release(o)
export {}
