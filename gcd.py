m = int(input())
n = int(input())

r = m % n

while r != 0:
    m = n
    n = r
    r = m % n

print(n)
