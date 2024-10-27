def memoize(func):
    """Декоратор для кэширования результатов функции."""
    cache = {}

    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]

    return wrapper


@memoize
def fibonacci(n):
    """Вычисляет n-е число Фибоначчи."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Пример использования
if __name__ == "__main__":
    for i in range(30):
        print(f"Fibonacci({i}) = {fibonacci(i)}")
