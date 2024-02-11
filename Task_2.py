#2
import re
from typing import Callable

def generator_numbers(text: str):
    # Знайти всі дійсні числа у тексті за допомогою регулярного виразу
    numbers = re.findall(r'\b\d+\.\d+\b', text)
    
    # Пройтися по кожному числу та повернути його через генератор
    for number in numbers:
        yield float(number)

def sum_profit(text: str, func: Callable):
    # Застосувати переданий генератор до тексту та підсумувати всі числа
    return sum(func(text))

# Приклад використання
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
