import random

arr = []
for i in range(0,10):
    arr.append(random.randrange(1, 100, 1))

print(arr)
print (len(arr))
print(max(arr))
print(min(arr))
arr.sort()
print(arr)
del arr[2]
print(arr)
del arr
print(arr)