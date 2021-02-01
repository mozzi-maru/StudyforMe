#작성중. 미완성파일

import math as mt
import random as rd

exp_now = 1
exp_gol = 100
level = 1


i=0
while i > 1000:
    exp_get = rd.randint(1, 100)
    exp_now = exp_now + exp_get
    if exp_now > exp_gol:
        level = level + 1
    print(exp_now)
    i = i +1

print(level)
