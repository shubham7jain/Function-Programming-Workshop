from functools import reduce
## accumulator - acc
def add(acc, x):
  return (acc + x)

### it starts with default value 0
sum = reduce(add, [1, 2, 3, 4, 5])
print(sum)
