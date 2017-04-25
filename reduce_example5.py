from functools import reduce
## with default value
sentences = ['A test', 'Another test', 'test and test']

count = reduce(lambda acc, x: acc + x.count('test'), sentences, 0)
print(count)
