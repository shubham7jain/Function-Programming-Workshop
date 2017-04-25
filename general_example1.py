def gt5(x):
  return x>5

print(any(gt5(x) for x in list(map(len, ['Tyler', 'James', 'Durden']))))
