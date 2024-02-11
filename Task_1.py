def caching_fibonacci():
    cache = {}  # словник для зберігання обчислених значень

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:  # перевіряємо, чи вже є значення в кеші
            return cache[n]
        else:
            # обчислюємо нове значення та зберігаємо його у кеші
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]

    return fibonacci

# Приклад використання
fib = caching_fibonacci()
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
#test