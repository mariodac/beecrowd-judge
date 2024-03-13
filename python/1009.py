salario_final = None
vendas_total = None
salario_fixo = None
nome = None

def read_string():
  try:
    # read for Python 2.x
    return input()
  except NameError:
    # read for Python 3.x
    return input()

def read_numeric():
  try:
    # read for Python 2.x
    return float(input())
  except NameError:
    # read for Python 3.x
    return float(input())


nome = read_string()
salario_fixo = read_numeric()
vendas_total = read_numeric()
salario_final = "{:0.2f}".format((salario_fixo + vendas_total * 0.15))
print(str("TOTAL = R$ ") + str(salario_final))