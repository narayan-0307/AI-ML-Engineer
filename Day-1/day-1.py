# print("Hello World")

#Avarage of 2 numbers

'''
num1 = 10.9
num2 = 5

avg = (num1 + num2 ) / 2

print("The Avg of 2 numbers is: ", avg)

'''
'''
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Hello", name + ", your are", age, "years old!")
'''

'''
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the first number: "))

#Sum (Addition)
sum = num1 + num2
print(int(sum))

#Difference (Substraction)
sum = num1 - num2
print(int(sum))

#Product (Multiplication)
sum = num1 * num2
print(int(sum))

#Quotient (Division)
sum = num1 / num2
sum = num1 / num2
print(int(sum))

'''

'''
int_1 = int(input("Enter the first Integer: "))
int_2 = int(input("Enter the second Integer: "))
float_1 = float(input("Enter the first Float: "))

converted_float_1 = float(int_1)
converted_float_2 = float(int_2)

avg = (converted_float_1 + converted_float_2 + float_1) / 2

print(avg)

'''

'''
my_str = input("Enter the number: ")

print("An Integer: ", int(my_str), type((my_str)), "\n", 
      "A Float: ", float(my_str), type(float(my_str)), "\n", 
      "A String: ", '"',my_str,'"', type(my_str))


'''

'''
#x = 10 + 3 * 2 ** 2
x = 10 + 3 *  2 ** 2

print(x) #Result: 22, ---> 1st: 2**2 = 4, 2nd: 4 * 3 = 12, 3rd: 12 + 10 = 22

'''

'''
#Swap Values of 2 numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the Second number: "))
num1, num2 = num2 , num1

print(num1, num2)
'''

'''
CelsiusTemp = float(input("Enter the tempreture: "))
FahrenheitTemp = (CelsiusTemp * (9/5)) + 32
print(FahrenheitTemp,"F")
'''

'''
#Area of Circle
r = float(input("Enter the radius: "))
PI = 3.14

area = PI * (r**2)

print("The area is: ",area)

'''

'''
principle = input("Enter the Principle (P): ")
rate = input("Enter the Rate (R): ")
time = input("Enter the time (T): ")

SI = (float(principle) * float(rate) * float(time)) / 100

print(SI)
'''

num = float(input("Enter the decimal number: "))

print(int(num))

fraction = num - int(num) #5.5 - 5
print(f".{str(fraction).split('.')[1]}") #"0.5" -> split at '.' -> ['0', '5'] -> [1] -> '5'