# n = int(input("Enter the number: "))
# i = 1
# while (i <= 10):
#     print(f"{n} * {i} = {n * i}")
#     i += 1

# phrase = "artificial intelligence"
# count = 0
# for ch in phrase:
#     # if (ch == 'i'):
#     if "I" in ch:
#         count += 1
# print(f"Count of i: {count}")

# word = 'artificial'
#
# count = 0
#
# for ch in word:
#     if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
#         count += 1
# print(f"Vowels count of = {count}")

# num = int(input("Enter the number: "))
#
# sum = 0
#
# for i in range(1, num + 1):
#     sum += i
#
# print(f"Sum of numbers: {sum}")

# def cal_factorial(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     return fact
#
# n = int(input("Enter the factorial number: "))
# step = " X ".join(str(i) for i in range(n, 0, -1))
# result = cal_factorial(n)
# # print(f"Result = {result}")
# print(f"{n}! = {step} = {result}")

# def even_number(a, b):
#     for num in range(a, b+1):
#         if num % 2 == 0:
#             print(num)
# even_number(1, 10)
#
# even_number = []

# n = int(input("Enter the number: "))
# i = 1
# while i <= 10:
#     print(f"{n} * {i} = {n * i}")
#     i += 1


# def cal_factorial(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= 1
#     return fact
#
# n = int(input("Enter the number: "))
# steps = " X ".join(str(i) for i in range(n, 0, -1))
# result = cal_factorial(n)
# print(f"{n}!: {steps} = {result}")

# def even_odd(a, b):
#     for num in range(a, b+1):
#         if num % 2 == 0:
#             print(num)
# even_odd(1, 10)

# text = "1409, D-WING,14 FLOOR, SRA SANJAY NAGAR WALBHAT ROAD, GOREGAON EAST.MAHARASHTRA – 400 063"
# result = text.title()
# print(result)

# for i in range(5, 0, -1):
#     print(i)

# def avg(a, b, c):
#     avg_result = a + b + c / 3
#     return  avg_result
#
# result = avg(12, 23, 34)
# print(result.__round__(2))

# def digits(n):
#     count = 0
#     while n > 0:
#         n = n // 10
#         count += 1
#     return count
# print(digits(321))

# def sum_digits(n):
#     sum = 0
#     while n > 0:
#         digit = n % 10
#         sum += digit
#         n = n // 10
#     return sum
# print(sum_digits(321))
# def count_digits(n):
#     count = 0
#     while n > 0:
#         digit = n % 10
#         # sum += digit
#         count += 1
#         n = n // 10
#     return count
# print(count_digits(32165))


# def number_digits(n):
#     while n > 0:
#         digit = n % 10
#         print(digit)
#         n = n // 10
# number_digits(2584436)

# for i in range(1, 101):
#     if (i % 3 == 0 and i % 5 == 0):
#         print(i)

# user_input = int(input("Enter a number: (or 'Quit' to exit)"))
# while True:
#     if user_input == "Quit":
#         print("Existing....")
#         break
#     else:
#         number = float(user_input)
#         if user_input > 0:
#             print(f"{number} Is Positive")
#         elif user_input < 0:
#             print(f"{number} Is Negative")
#         else:
#             print("Invalid User Input")
#     user_input = int(input("Enter a number: (or 'Quit' to exit)"))

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(1, n-1):
#         if n % i == 0:
#             return False
#     return True
# num = int(input("Enter the number: "))
# if is_prime(num):
#     print(f"{num} is prime number")
# else:
#     print(f"{num} is not prime number")

import random

def number_guessing_game():
    random_numner = random.randint(1, 100)
    attempt = 0

    while True:
        user_guess = int(input("Enter the number between 1 to 100: "))
        attempt += 1

        if user_guess < random_numner:
            print("Too Low")
        elif user_guess > random_numner:
            print("Too High")
        else:
            print(f"Congratulation you guessed right nunber - {user_guess} with {attempt}")
            break
number_guessing_game()
