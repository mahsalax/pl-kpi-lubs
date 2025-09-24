#Порахувати кількість чисел, що більші за 5.
import random
numbers = [random.randint(1, 10) for _ in range(10)]
mth5 = sum(1 for num in numbers if num > 5)
print("Список випадкових чисел:", numbers)
print("Кількість чисел, що більші за 5:", mth5)


