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
