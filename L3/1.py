# Створити список з 10 випадкових чисел. Знайти їх суму.
import random  
numbers = [random.randint(1, 100) for _ in range(10)]
_sum = sum(numbers)
print("Список випадкових чисел:", numbers)
print("Сума чисел у списку:", _sum)



