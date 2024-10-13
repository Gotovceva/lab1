#Лабараторная работа № 3
#Уровень 1, задание 4
#Найдите среднее значение элементов массива размером 5.  Преобразовать исходный массив , вычитая из каждого элемента полученное значение
array = [10.0, 35.0, 60.0, 5.0, 15.0]
average = sum(array)/len(array)
transformed_array = [x - average for x in array]
print(transformed_array)
exp_result = [-15.0, 10.0, 35.0, -20.0, -10.0]
if transformed_array != exp_result:
    print("Программа работает неверно")
else:
    print("Программа написана верно")
