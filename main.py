from array_ds import ArrayDS
from ordered_array_ds import OrderedArrayDS

array_size = 10
arr = OrderedArrayDS(array_size)

arr.insert(10)
arr.insert(22)
arr.insert(99)
arr.insert(79)
arr.insert(43)
arr.insert(10)
print(arr)
arr.delete(22)
print(arr)
