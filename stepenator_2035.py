def combination(n, k):
    ##C(n,k)
    if k < 0 or k > n:
        return 0
    k = min(k, n - k)
    numerator = 1
    denominator = 1
    for i in range(k):
        numerator *= (n - i)
        denominator *= (i + 1)
    return numerator // denominator

def solve_combinatorial(k):
    if k == 1:
        return 1
    count = 0
    for L in range((k + 1) // 2, k):
        r = k - L
        if r < 1 or r > L:
            continue
        count += combination(L - 1, r - 1)
    return count % (10**9 + 7)

if __name__ == '__main__':
    n = int(input())
    a = []
    for _ in range(n):
        a.append(tuple(map(int, input().split())))
    for i in range(n):
        print(solve_combinatorial(a[i][1]))

def solve(k):
    if k == 1:
        return 1
    count = 0
    left = (k + 1) // 2
    for L in range(left, k):
        r = k - L
        if r < 1 or r > L:
            continue
        for b in range(2**(L-1), 2**L):
            if count_func_cal(b) == k:
                count += 1
    return count % (10**9 + 7)

def count_func_cal(b):
    bin_b = bin(b)[2:]
    l = len(bin_b)  # число битов
    r = bin_b.count('1')  # число единиц
    return r + l