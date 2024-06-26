from functools import reduce


# id = 206132755
# age = 26.9
# name = 'Ali'
# is_male = True
# #----------------------------------------------------------------------
# print("Hello, My name is", name, "I'm", age, "years old & my id is", id)
# #----------------------------------------------------------------------
# print(type(id))
# print(type(age))
# print(type(name))
# print(type(is_male))
# #----------------------------------------------------------------------
# age1 = input("enter your age: ")
# age1 = float(age1)
# if type(age1) == type(float):
#     pass
# isOld = age1 > 37
# if isOld:
#     print("you are old")
# else:
#     print("you are young")
# #----------------------------------------------------------------------
# answer = input("how are you: ")
# while answer != "good":
#     answer = input("wrong answer try again!!: ")
# print("you are good!!")
# #----------------------------------------------------------------------
# ans = int(input("5 * 2 = "))
# if ans == 10:
#     print("correct")
# else:
#     while ans != 10:
#         ans = int(input("wrong answer try again!!: 5 * 2 = "))
#     print("correct")
# #----------------------------------------------------------------------
# for i in [1,2.5,'A',"Ali",-3]:
#     print(i)
# ind = 0
# #----------------------------------------------------------------------
# while ind <= 3:
#     print(ind)
#     ind = ind + 1
# #----------------------------------------------------------------------
# for num in [3,5,8,1,-4,7,-8]:
#     if num < 0:
#         print(num)
#         break
# #----------------------------------------------------------------------
celsius_temperatures = [20,22,25,27,30,33]
fahrenheit_temperatures = list(map(lambda x : (x * 9/5) + 32, celsius_temperatures))
filrered_temps = list(filter(lambda x : x >= 75, fahrenheit_temperatures))
average_temp = reduce(lambda x,y : x + y, fahrenheit_temperatures)/len(fahrenheit_temperatures)
print(fahrenheit_temperatures)
print(filrered_temps)
print(average_temp)
