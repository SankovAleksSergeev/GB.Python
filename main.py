# parta1 = int (input ("Введите кол-во учащихся в первом классе > "))
# parta2 =int (input ("Введите кол-во учащихся во втором классе > "))
# parta3 =int (input ("Введите кол-во учащихся во третим классе > "))

# parta1 = parta1 //2 +parta1%2
# parta2 = parta2//2 +parta2%2
# parta3 = parta3//2 +parta3%2

# print ("Необходимое кол-во парт = ",(parta1+parta2+parta3))

# ------------------------------------------------------------------------------
# a = int (input("Введите номер вагона Вити > "))
# b = int (input("Введите кол-во пройденых вагонов > "))
# if a<b:
#     print("Вагонов в электрички = ", a+b-1)
# else: print ("Без дополнительной информации узнать кол-во вагон не возможно")

# ====----------------------------------------------------------------------------

# year = int(input('Введите год > '))

# if year %4==0 or year%400==0:
#     print('yes')
# else: print("no")



# a = 3
# b = 5
# c = 10

# if a<b:
#     if (c%a==0 and c<a*b) or (c%b==0):
#         print("yes")
#     else: print ("no")
# elif a>b:
#     if (c%b==0 and c<a*b)or(c==a):
#         print("yes")
#     else:print ("no")
# elif a==b:
#     if (c%a==0):
#         print("yes")
#     else: print ("no")

    
# x= "stroka" 
# for i in x:
#     print(i)

# list = range(0,10)
# print(*list)



# factorial = int (input('Введите число > '))
# res=1
# x=1
# while factorial>x:
#     res = res+(res * x)
#     x+=1
# print(res) 



# n = int (input("Введите кол-во дней > "))
# i=1
# count = 0
# max = 0
# while i <= n:
#     temp = int (input("Введите в {i} день температуру > "))
#     if temp >= 0:
#         count+=1
#         if count > max:
#             max = count
#     else: count =0
#     i+=1
# print(max)


# list_1 = []

# for i in range(5):
#     list_1.append(i)
# print(*list_1)


# a = [2,3,4,6]
# print(a.insert(0, 25))
# print(a)
        


# list_1 = [1, 2, 3,3, 4, 5]
# k = 3
# count = 0
# for i in range(len(list_1)):
#     if list_1[i] == k:
#         count +=1 
# print(count)


 

# list_1 = [1,2, 3, 6, 5,7,9,8,18,12]
# k = 4
# minraz = (k - list_1[0])**2
# b = 0 
# i = 0 
# while i < len(list_1):
#     if (k-list_1[i])**2 <= minraz:
#         minraz = (k-list_1[i])**2
#         b = i
#     i += 1
# print(list_1[b])


# x = {'A':1, 'E':1, 'I':1, 'O':1, 'U':1, 'L':1, 'N':1 , 'S':1, 'T':1, 'R':1,'D':2, 'G':2,'B':3, 'C':3, 'M':3, 
#     'P':3,'F':4, 'H':4, 'V':4, 'W':4, 'Y':4,'K':5,'J':8, 'X':8,'Q':10, 'Z':10,'А':1, 'В':1, 'Е':1, 'И':1, 'Н':1, 
#     'О':1, 'Р':1, 'С':1, 'Т':1, 'Д':2, 'К':2, 'Л':2, 'М':2, 'П':2, 'У':2, 'Б':3, 'Г':3, 'Ё':3, 'Ь':3, 'Я':3,'Й':4, 'Ы':4,
#     'Ж':5, 'З':5, 'Х':5, 'Ц':5, 'Ч':5, 'Ш':8, 'Э':8, 'Ю':8, 'Ф':10, 'Щ':10, 'Ъ':10}
# x = {q.lower(): x[q] for q in x}
# e=0
# k= input('d')

# for j in x: 
#     for i in range(len(k)):
#         if j.format(j, x[j]) == k[i]:
#             e = e+x[j]
# print(e)



# spisok = [int(i)for i in input("Введите числа > ").split()]

# print(*spisok)


# ----------------------------------------------------------------

#  дан список чисел. Определите, сколько в вем встречаюся различных чисел


# x = list()
# x = [1,1,1,2,2,2,3,3,4,5,5]
# x= set(x)
# print(len(x))


# -----------------------------------------------------------------------


# spisok = [1,2,3,4,5,6,7]
# k = int(input ("d"))
# spisok= spisok[len(spisok)-k:len(spisok):] + spisok[0:len(spisok)-k:]  
# print(spisok)