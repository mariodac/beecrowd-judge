# 1008 	Salário

cod = None
horas = None
salario = None
valorDaHora = None

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


cod = read_integer()
horas = read_integer()
valorDaHora = read_numeric()
salario = "{:0.2f}".format((horas * valorDaHora))
print(str("NUMBER = ") + str(cod))
print(str("SALARY = U$ ") + str(salario))