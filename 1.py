# Лабараторная работа № 1
# 8 задание 1 уровень
# Вычислить s=1!+2!+...+6!
s = 0
x = 1
for i in range(1,7):
    x = x*i
    s += x
print(s)

# 1 уровень задание 4
№ Вычислить s = cosx+cos2x/x+cos3x/x^2+...+cos9x/x^8
import math
s = 0
x = int(input())
for n in range(1,10):
    i = math.cos(n*x)/(x**(n-1))
    s += i
print(s)

# 1 уровень задание 9
# Вычислить s = (-1)^1*5^1/1!+(-1)^2*5^2/2!+...+(-1)^6*5^6/6!
s = 0
a = 1
x = 5
for i in range(1,7):
    a = a * i
    t = ((-1)**i)*(x**i)/a
    s += t
print(s)



