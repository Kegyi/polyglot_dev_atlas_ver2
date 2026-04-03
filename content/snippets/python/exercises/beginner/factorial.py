def factorial(n: int) -> int:
    r = 1
    for i in range(2, n+1):
        r *= i
    return r

if __name__ == '__main__':
    try:
        n = int(input().strip())
    except Exception:
        n = 5
    print(factorial(n))
