#Сформувати список квадратів усіх елементів.
import random
numbers = [random.randint(1, 10) for _ in range(10)]
sqr = [num ** 2 for num in numbers]
print("Список випадкових чисел:", numbers)
print("Список квадратів усіх елементів:", sqr)
