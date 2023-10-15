from array_ds import ArrayDS

array_size = 10
arr = ArrayDS(array_size)

arr.insert(10)
arr.insert(22)
arr.insert(99)
print(arr)
arr.delete(22)
print(arr)
