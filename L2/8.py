import random
for i in range(len(arr)):
    if arr[i] < 0:
        arr[i] = -arr[i]
print("Масив без від’ємних:", arr)