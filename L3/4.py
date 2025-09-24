#Замінити всі від’ємні числа на `0`.
import random
numbers = [random.randint(-50, 50) for _ in range(10)]
replaced = [num if num >= 0 else 0 for num in numbers]
print("Список випадкових чисел:", numbers)
print("Список після заміни від’ємних чисел на 0:", repalced)
