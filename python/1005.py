# 1005 	Média 1

a = None
b = None
media = None

def read_numeric():
  try:
    # read for Python 2.x
    return float(input())
  except NameError:
    # read for Python 3.x
    return float(input())


a = read_numeric()
b = read_numeric()
media = "{:0.5f}".format(((a * 3.5 + b * 7.5) / (3.5 + 7.5)))
print(str("MEDIA = ") + str(media))