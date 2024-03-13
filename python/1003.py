from numbers import Number

a = None
b = None
soma = None

def read_integer():
  try:
    # read for Python 2.x
    return int(input())
  except NameError:
    # read for Python 3.x
    return int(input())


a = read_integer()
b = read_integer()
soma = (soma if isinstance(soma, Number) else 0) + (a + b)
print(str("SOMA = ") + str(soma))