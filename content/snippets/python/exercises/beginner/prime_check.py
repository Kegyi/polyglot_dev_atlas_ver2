import math

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

if __name__ == '__main__':
    try:
        n = int(input().strip())
    except Exception:
        n = 97
    print(str(is_prime(n)).lower())
