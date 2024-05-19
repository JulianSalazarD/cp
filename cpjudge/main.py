x = int(input())
n = int(input())
numeros = input()
numeros = list(map(int, numeros.split()))
numeros.sort()
for p in numeros:
    if p*p > x:
        print(1, x)
        break
    n = x // p    
    if x % p == 0 and n in numeros:
        print(p, n)
        break

