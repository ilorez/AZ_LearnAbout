from functools import lru_cache
cache = {}
@lru_cache(maxsize=3000)
def fact(n): 
    if n == 1:
        return 1
    cache[n]=n * fact(n-1)
    return cache[n]
print(fact(999))