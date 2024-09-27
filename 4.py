# Лабараторная работа № 2
# Задание 3, уровень 1
# Для заданных a и b получить c = max(a,b), если a>0 или c =min(a,b), если a <= 0
a = int(input())
b = int(input())
if a > 0:
    c = max(a,b)
    print(c)
else:
    if a <= 0:
        c = min(a,b)
        print(c)
        
