'''
username =  input("Enter your username: ")
password =  input("Enter your password: ")

if username == 'admin' and password == 'pass':
    print("You are the successfully logged In")
elif username != 'admin':
    print("Wrong Username")
elif password != 'pass':
    print("Wrong Password")
else:
    print("Invalid credentials")

'''

'''
n = int(input("Enter the number: "))

i = 1

while ( i <= 10):
    print(f"{n} * {i} = {n * i}")
    i += 1
'''
'''
phrase = "artificial intelligence"

count = 0

for ch in phrase:
    if (ch == 'i'):
        count += 1

print("Count of i: ", count)
'''
'''
#Print Vowel count of given a string
word = "artificial"

count = 0

for ch in word:
    if ( ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
        count += 1
print("Vowels count of = ", count)
'''

'''
#Print sum of first 'n' natural numbers
num = int(input("Enter the number: "))

sum = 0

for i in range(1, num + 1):
    sum += i

print("Sum of numbers: ", sum)
'''
'''
def avg (a, b, c):
    cal_avg = (a + b + c) /3
    return cal_avg

print(avg(10,20,30))
'''

'''
#Factorial natural Numbers
def calc_factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
    
n = int(input("Enter your number: "))
steps = " X ".join(str(i) for i in range(n, 0, -1))
result = calc_factorial(n)
print(f"{n}! = {steps} = {result}")

# print(calc_factorial(n))

'''

'''
salary = float(input("Enter your salary: "))

if salary < 30000:
    print("5%")
elif salary <= 30000 and salary >= 70000:
    print("15%")
elif salary > 70000:
    print("25%")
else:
    print("Invalid input")
'''

'''
#Print even numbers in a given range
def even(a, b):
    for num in range(a, b + 1):
        if num % 2 == 0:
            print(num)

even(1, 10)

'''

'''
def print_digits(n):
    while n > 0:
        digit = n % 10       # get last digit
        print(digit)         # print it
        n = n // 10          # remove last digit

print_digits(312)
    

'''

'''
def count_number_digits(n):
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count

num = int(input("Enter the number: "))
result = count_number_digits(num)
print("Number of digits: ", result)

'''

'''
def sum_of_digits(n):
    sum = 0 
    while n > 0:
        digit = n % 10
        sum += digit
        n = n // 10
    return sum

print(sum_of_digits(1234))
'''

#print all number 1 to 100 which are divisible by 3 and 5
'''
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print(num)
'''

#Continusly ask user to enter a number until they enter a positive number and negative number until they user enter "Quit"

'''
user_input = input("Enter a number (or 'Quit' to exit): ")

while True:
    if user_input == "Quit":
        print("Exiting...")
        break
    else:
        number = float(user_input)
        if number > 0:
            print("Positive number: ", number)
        elif number < 0:
            print("Negative number: ", number)
        
    user_input = input("Enter a number (or 'Quit' to exit): ")
'''

'''
def calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b
    else:
        return "Invalid operation"

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter operation (+, -, *, /): ")

result = calculator(num1, num2, operation)
print("Result:", result)

'''

'''
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n -1 ):
        if n % i == 0:
            return False
    return True

num = int(input("Enter the number: "))
if is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")

''' 

#Number guessing game 

import random

def number_guessing_game():
    random_numbers = random.randint(1, 100)
    attempts = 0
    
    while True:
        user_guess = int(input("Guess the number bwtween 1 to 100: "))
        attempts += 1

        if user_guess < random_numbers:
            print("Too low")
        elif user_guess > random_numbers:
            print("Too high")
        else:
            print("Congratulations! You guessed the number in", attempts, "attempts.")
            break

number_guessing_game()
