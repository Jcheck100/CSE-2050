def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)


def fib(n, cache = {}):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    if n in cache:
        return cache[n]
    
    cache[n] = fib(n-1, cache) + fib(n-2, cache)

    return cache[n]

print(fib(1000))

def reversestring(s):
    if len(s) == 0:
        return s
    return reversestring(s[1:]) + s[0]

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

