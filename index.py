def factorial(n):
    if n <= 1: return 1
    return n * factorial(n - 1)

def fibonacci(n, memo=dict()):
    if n <= 0: return 1
    if n in memo: return memo[n]
    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]

print(fibonacci(100))