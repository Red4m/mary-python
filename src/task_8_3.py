"""Описать функцию Sin1( x , ε ) вещественного типа (параметры x , ε —
вещественные, ε > 0), находящую приближенное значение функции sin( x ):
sin( x ) = x – x ^3 /(3!) + x^ 5 /(5!) – ... + (–1) ^ n · x^( 2·n+1) /((2· n +1)!) + ... .
В сумме учитывать все слагаемые, модуль которых больше ε . С помощью
Sin1 найти приближенное значение синуса для данного x при шести данных
ε ."""

def fact (n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

def addendum (x, m):
    return x ** m / fact(m)

def sin1 (x, e):
    sin = x
    m = 3
    counter = 1
    while(True):
        if addendum(x, m) > e:
            if counter % 2 == 1:
                sin -= addendum(x, m)
            else:
                sin += addendum(x, m)
            m += 2
            counter += 1
        else:
            break
    print('sin', x, sin, '(e =', e, ')')


x = float(input('Enter x: '))
for j in range(6):
    while True:
        e = float(input('Enter e (very small number): '))
        if e > 0:
            break
    sin1(x, e)
