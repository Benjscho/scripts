import sys

def sieve(n: int):
    arr = [1 for i in range(n)]
    arr[0] = 0
    arr[1] = 0
    i = 2
    while i*i < n:
        if arr[i] == 1:
            for j in range(i*i, n, i):
                arr[j] = 0
        i += 1

    primes = []
    for j in range(n):
        if arr[j] == 1:
            primes.append(j)
    return primes

if __name__ == '__main__':
    if sys.argv[1]:
        print(sieve(int(sys.argv[1])))
    else:
        print(sieve(2000))
