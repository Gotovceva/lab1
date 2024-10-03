# Лабараторная работа №1
#3 уровень, задание 3
#Вычислить сумму s, прекращая суммирование, когда очередной член суммы по абсолютной величине станет меньше 0,0001, при изменении аргумента x в указанном диапазоне [a,b] с шагом h. Для сравнения в каждой точке вычислить функцию, являющаюся аналитическим выражением ряда S = 1+《 cos(ix)/ i!,  y =e^cosx×cos(sinx), a = 0,1 b = 1 h = 0,1

import math
a = float(0.1)
b = float(1)
h = float(0.1)
q = 0
i = 0
y = 0
s = 0
j = float(0.0001)
while a <= b:
    q = 1
    s = (math.cos(1*a)/math.factorial(1))
    i = 1
    while abs(s) >= j:
        i += 1
        q = q + s
        s = (math.cos(i*a)/ math.factorial(i))
    y = math.cos(math.sin(a))*math.exp(math.cos(a))
    print(a,q,y,j)
    a += h








