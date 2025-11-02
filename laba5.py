arr = [1, 2, 3, 4, 5]
a = [i ** 2 for i in arr]
zip_pair = list(zip(arr, a))
print(zip_pair)

from functools import reduce
def sumkvadrat(x, y):
    return x + y

sum_kvadr = reduce(sumkvadrat, a)
print(sum_kvadr)
