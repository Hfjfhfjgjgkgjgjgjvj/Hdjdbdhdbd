from numbers import Number

Count = None


for count in range(166):
  Count = (Count if isinstance(Count, Number) else 0) + 1
  print(Count)
