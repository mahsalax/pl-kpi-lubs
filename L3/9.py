#Вивести індекси всіх елементів, які дорівнюють мінімальному.
import random
numbers = [random.randint(1, 100) for _ in range(10)]
min_number = min(numbers)
min_indixes = [index for index, num in enumerate(numbers) if num == min_number]
print("Список випадкових чисел:", numbers)
print("Мінімальний елемент списку:", min_number)
print("Індекси елементів, які дорівнюють мінімальному:", min_indixes)
