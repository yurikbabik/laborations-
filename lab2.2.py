from math import *
def fun():
    a = -1
    term = 0.0
    b = -0.9
    h = 0.01
    d = 0.001

    x = a
    while x <= b:
        suma = 0
        k = 2
        term = ((-1)**k * cos(k * x)) / (k**2 - 1)
        while abs(term) > d:
             suma += term
             k += 1
             term = ((-1) ** k * cos(k * x)) / (k ** 2 - 1)
        print(f"x = {x}, sum = {suma}")
        x = round(x + h, 2)
fun()
