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


a = [2,3,4,6]
print(a.insert(0, 25))
print(a)
        


