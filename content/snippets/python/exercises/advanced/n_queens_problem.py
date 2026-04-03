N=8
cols=[0]*N

def ok(r,c):
    for i in range(r):
        if cols[i]==c or abs(cols[i]-c)==r-i: return False
    return True

def solve(r):
    if r==N:
        print(cols); return True
    for c in range(N):
        if ok(r,c):
            cols[r]=c
            if solve(r+1): return True
    return False

if __name__=='__main__': solve(0)
