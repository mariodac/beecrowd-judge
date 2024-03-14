# 1014 	Consumo

consumo = None
y = None
x = None

def read_integer():
  try:
    # read for Python 2.x
    return int(input())
  except NameError:
    # read for Python 3.x
    return int(input())

def read_numeric():
  try:
    # read for Python 2.x
    return float(input())
  except NameError:
    # read for Python 3.x
    return float(input())


x = read_integer()
y = read_numeric()
consumo = x / y
print(str("{:0.3f}".format(consumo)) + str(" km/l"))