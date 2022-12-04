import re

c = "Jazmine Holcomb 3212 Adams Avenue Washington MD eluir.azevedo.70@lucidmode.com"
# d = re.compile("^([A-Z][a-z]+) ([A-Z][a-z]+)")
# d = re.compile("([0-9]+) (([A-Za-z_]+ )+)([A-Za-z_]+) ([A-Z][A-Z])")
d = re.compile("([0-9]+ ([A-Za-z_]+ )+)([A-Za-z_]+) ([A-Z][A-Z])")
# d = re.compile("[A-Za-z0-9\.\-+_]+@[A-Za-z0-9\.\-+_]+\.[a-z]+")

a = re.findall(d, c)
print(a)