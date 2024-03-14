# 1006 	Média 2

media = None
a = None
c = None
b = None

def read_numeric():
  try:
    # read for Python 2.x
    return float(input())
  except NameError:
    # read for Python 3.x
    return float(input())


a = read_numeric()
b = read_numeric()
c = read_numeric()
media = "{:0.1f}".format((((a * 2 + b * 3) + c * 5) / ((2 + 3) + 5)))
print(str("MEDIA = ") + str(media))