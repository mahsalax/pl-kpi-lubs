#Знайти добуток усіх елементів.
import random
numbers = [random.randint(1, 10) for _ in range(10)]
dob = 1
for num in numbers:
    dob *= num
print("Список випадкових чисел:", numbers)
print("Добуток усіх елементів списку:", dob)
