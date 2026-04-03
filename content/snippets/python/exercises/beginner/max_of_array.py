import sys

def max_of_array(arr):
    return max(arr) if arr else None

if __name__ == '__main__':
    try:
        parts = sys.stdin.read().strip().split()
        if parts:
            n = int(parts[0]); vals = list(map(int, parts[1:1+n]))
        else:
            n = 5; vals = [1,2,3,4,5]
    except Exception:
        n = 5; vals = [1,2,3,4,5]
    print(max_of_array(vals))
