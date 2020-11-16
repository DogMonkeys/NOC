WALK = 550
RAN = 700
RAP = 350
SWIM = 600
ALL = [RAN, RAP, SWIM, WALK]

from json import loads
from os import getcwd
print(getcwd())
f = open('Data\\foods.json', encoding='utf-8')
dt_tmp = f.read()
f.close()
FOODS = loads(dt_tmp)
del dt_tmp