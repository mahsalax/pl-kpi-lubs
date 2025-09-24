n = int(input("Введи число: "))
prime = True
if n < 2:
    prime = False
for i in range(2, n):
    if n % i == 0:
        prime = False
        break
if prime:
    print("Просте")
else:
    print("Не просте")