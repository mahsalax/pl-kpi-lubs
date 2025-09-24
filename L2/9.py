import random
all_even = True
for x in arr:
    if x % 2 != 0:
        all_even = False
        break
if all_even:
    print("Всі парні")
else:
    print("Є непарні")