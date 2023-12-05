from numbers import Number

Count = None


for count in range(int(float('inf'))):
  Count = (Count if isinstance(Count, Number) else 0) + 1
  print(Count)
