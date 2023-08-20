# print("Hello world")



# # ctrl kf= close a project folder
# # ctrl backlash (~)= open folder
# #to run a program = py/python filename.py
# #you can run a code as either shell or script
# #syntax;
# # symbol/symbol = value

# last_name = "oyegbemi"
# first_name = "ayodamola"
# is_male = True
age = 30
# salary = 63337377734.56
# print("last_name type is", type(last_name))
# print("is_male type is", type(is_male))
#print("age type is", type(age))
# print("salary type is", type(salary))

# print("the class of the syntax is",type("age"))
#
# x, y, name, is_cool = (1, 2.5, "folorunsho", True)
# print(x, y, name, is_cool)



# num1 = 12
# num2 = 19
# mult = num1 * num2
# div = num2/num1
# modulus = num2 % num1
# exp = num1**num2

# print("num1 * num2 =", mult)
# print("num2 / num1 =", div)

# classwork
# try out conversion- int and float, as we have done for str and int
# try out modulus and exponential 

# print("num2 % num1 =", modulus)
# # print("num1 ** num2 =", exp)

# from pickletools import anyobject


# salary =int(445000)
# name = int("ayo")
# # r = str(salary)
# print(salary)
# # print(name)
# # print(type(r))
# # print(r)

# # print("the class type is",type(salary))
# print(s)


# num = 14
# # print(type(num))
# new_num = str(num)
# print(type(new_num))


# num = 147.9
# # print(type(num))
# new_num = bool(num)
# print(type(new_num))

# single quote [''] and double quote[""] are used for the same function
# triple quote['''num'''] is used to better format your notes; allows spacing, enter etc


# l1 = [3,5,2,4]
# newtuple = tuple(l1)

# print(newtuple)

# dir(l1)
# print(type(l1))
# print(dir(l1))


# functions

def addingMachine(x,y):
    sum = x + y
    return sum

output1 = addingMachine(12,7)
output2 = addingMachine(3,85)
output3 = addingMachine(15,9)


# print(output1 + output2 + output3)

def calculation(x,y):
    sum = x + y
    return sum

result= calculation(2,7)
print(result)

# conditionals

# age = 24

# if age >= 25:
#     print("The young lady can marry and vote")
# elif age > 18:
#     print("the young lady cannot marry or vote")
# else:
#     print("the young lady is a minor and cannot vote")

def sayHello():
    name = 'Good morning Tunde'
    # print(name)
    return name
result= sayHello()
print(result)

#. 1. PErform a task in it and print result
#. 2. perform a task and RETURN result

# result = sayHello()

# print(result)

def addingMachine(x,y=34):
    sum = x + y
    return sum

output1 = addingMachine(12,7)
output2 = addingMachine(2,17)
output3 = addingMachine(1,37)
output4 = addingMachine(7)

grandresult = output1 + output2 + output3 + output4
print(f'Grand Result {grandresult}')

# age = 60

# if age >= 23 and age < 45:
#     print('The young lady is in her prime')
# elif age > 20: 
#     print('The young yoruba lady cannot wed yet but can vote ')
# else:
#     print('Sorry she is a minor and thus cannot vote or marry')



s1 = {'fname':'Ayo','gender':'Male','ethnic':'Yoruba','age':30}
s2 = {'fname':'kemi','gender':'feMale','ethnic':'Yoruba','age':20}
s3 = {'fname':'Danladi','gender':'Male','ethnic':'Hausa','age':40}
# print(s2['age'])

students = [
    {'fname':'Ayo','gender':'Male','ethnic':'Yoruba','age':30},
    {'fname':'kemi','gender':'feMale','ethnic':'Yoruba','age':20},
    {'fname':'Danladi','gender':'Male','ethnic':'Hausa','age':40}
]

print(s2["ethnic"])


l1 = [23,6,7,5,98,4,0,333,4,6,5,77]

for item in l1:
    if item >= 7:
        print(item)

# age = 24

# if age >= 25:
#     print("The young lady can marry and vote")
# elif age > 18:
#     print("the young lady cannot marry or vote")
# else:
#     print("the young lady is a minor and cannot vote")