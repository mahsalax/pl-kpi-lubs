import random
arr = []
for i in range(8):
    arr.append(random.randint(-100, 100))  # випадкові числа від -100 до 100
print("Початковий масив:", arr)

arr.sort()
print("Відсортований масив:", arr)