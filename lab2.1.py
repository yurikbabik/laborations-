from math import *

a = 1
b = 3.5
h = 0.2


while a <= b:
    result = 0
    if a < 2:
        result = cos(e**a)
    elif 2 <= a < 3:
        result = 1 /cos(log(a))
    else:
        result = sin(log(a))
    print(f"x = {a} f(x) = {result}" )
    a = round(a + h, 2)




