# import os
# os.system('cls') 
# print("Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).")
# print('Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.')
# print('Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.')
# print('Затем пользователь вводит сами элементы множеств.')
# print("")


# many_1 = set()
# many_2 = set()
# for j in range(int(input('Введите размер 1 множества и его элементы > '))):
#     x = input(' элемент > ')
#     many_1.add(x)

# for j in range(int(input('Введите размер 2 множества и его элементы > '))):
#     x=input(" элемент > ")
#     many_2.add(x)

# sorting = list (many_1.union(many_2))
# sorting.sort()
# print('Элементы двух множеств в порядке возрастания без повторения: ',*sorting)




# ----------------------------------------------------------------------------------------------------------------------------
import os
os.system('cls') 
print('Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности.')
print('Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.')
print('Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.')
print('В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих')
print('модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.')
print('Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,')
print('находясь перед некоторым кустом заданной во входном файле грядки.')
print('')
from random import randint
Number_Berries = list(randint(1,100) for i in range(int (input('Введите кол-во кустов > '))))

if len(Number_Berries)<3:
    print("")
    print("Кусты высажены по кругу, их не может быть меньше 3!")
else: 
    print("")
    print("Количество ягод на каждом кусту > ", Number_Berries)
    res_1 = Number_Berries[0]+ Number_Berries[1]+ Number_Berries[len(Number_Berries)-1]
    res_2 = Number_Berries[0] + Number_Berries[len(Number_Berries)-1] + Number_Berries[len(Number_Berries)-2]
    res_3 = Number_Berries[0]+ Number_Berries[1]+ Number_Berries[2]
    if res_1>res_2:
        result = res_1
    else : result  = res_2
    if result<res_3:
        result = res_3
    res = 0
    for i in range(len(Number_Berries)):
        res = res + Number_Berries[i]
        if i > 2:
            res = res - Number_Berries[i-3]
            if res > result:
                result=res
    print("Максимальное кол-во ягод с трех кустов : ",result)
