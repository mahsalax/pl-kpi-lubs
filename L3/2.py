#Вивести всі парні елементи списку
import random
numbers = [random.randint(1, 100) for _ in range(10)]
p_numbers = [num for num in numbers if num % 2 == 0]
print("Список випадкових чисел:", numbers)
print("Парні елементи списку:", p_numbers)
