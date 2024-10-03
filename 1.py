# Лабараторная работа № 1
# 8 задание 1 уровень
# Вычислить s=1!+2!+...+6!
x = 0
for i in range(1,7):
    y = 1
    for q in range(1,i+1):
        y = y * q
    x += y
print(x)
