# Лабараторная работа № 1
#Уровень 2, задача 7
# Начав тренировки спортсмен в первый день пробежал 10 км. Каждый следующий день он увеличивал дневную норму на 10 процентов от нормы предыдущего дня. определить какой суммарный путь пробежит спортсмен за 7 дней
s = 10
a = 0
i = 1
while i <= 7:
    s = 10 * 1.1 ** i
    a = a + s
    i += 1
print(a)

# Уровень 2 задание 9
# Вкладчик положил в банк 10000 рублей под 8 % в месяц. Определить через какое время сумма удвоится
s = 10000
procent = 1.08
n = 0
while s < 20000:
    n += 1
    s *= procent
print("Через ", n, "лет")

# Уровень 2 задание 5
# Определить частное и остаток от деления двух целых чисел используя операцию вычитания
print("Введите делимое: ")
n = int(input())
print("Введите делитель: ")
m =int(input())
c = 0
o = 0
while n > m:
    n -= m
    c += 1
    if n - m < 0:
        o = n
        break
print("Целая часть от деления ",c)
print("Остаток от деления ",o)

