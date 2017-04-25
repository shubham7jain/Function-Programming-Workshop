from functools import reduce
## with default value
sentences = ['A test', 'Another test', 'test and test']

def test_count(acc, x):
  return (acc + x.count('test'))
  
count = reduce(test_count, sentences, 0)
print(count)
