#Знайти максимальний елемент списку без `max()`.
import random
numbers = [random.randint(1, 100) for _ in range(10)]
max_number = numbers[0]
for num in numbers:
    if num > max_number:
        max_number = num
print("Список випадкових чисел:", numbers)
print("Максимальний елемент списку:", max_number)
