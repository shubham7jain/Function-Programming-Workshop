from functools import reduce
sum = reduce(lambda acc, x: acc + x, [1, 2, 3, 4, 5])
print(sum)
