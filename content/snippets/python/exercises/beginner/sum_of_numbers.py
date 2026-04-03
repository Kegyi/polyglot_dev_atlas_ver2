def sum_n(n: int) -> int:
    return n * (n + 1) // 2

if __name__ == '__main__':
    try:
        n = int(input().strip())
    except Exception:
        n = 10
    print(sum_n(n))
