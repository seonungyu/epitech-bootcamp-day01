# OEIS "n, prime(n) for n = 1..10000" 표와 같은 형식(n 소수)의 primes.txt를 만든다
primes = []
n = 2
while len(primes) < 10000:
    if all(n % p for p in primes if p * p <= n):
        primes.append(n)
    n += 1
with open("primes.txt", "w") as file:
    for i, p in enumerate(primes, start=1):
        file.write(f"{i} {p}\n")
