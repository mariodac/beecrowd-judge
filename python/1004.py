# 1004 	Produto Simples

prod = None
b = None
a = None

def read_integer():
  try:
    # read for Python 2.x
    return int(input())
  except NameError:
    # read for Python 3.x
    return int(input())


a = read_integer()
b = read_integer()
prod = a * b
print(str("PROD = ") + str(prod))