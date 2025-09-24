#Вивести елементи списку у зворотному порядку.
import random
numbers = [random.randint(1, 100) for _ in range(10)]
revnum = numbers[::-1]
print("Список випадкових чисел:", numbers)
print("Список у зворотному порядку:", revnum)

