# 1002 	Área do Círculo

import math

area = None
raio = None
PI = None

def read_numeric():
  try:
    # read for Python 2.x
    return float(input())
  except NameError:
    # read for Python 3.x
    return float(input())


PI = 3.14159
raio = read_numeric()
area = "{:0.4f}".format((PI * (math.pow(raio, 2))))
print(str("A=") + str(area))