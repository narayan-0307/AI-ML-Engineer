# def count_number(n):
#     count = 0
#     while n > 0:
#         n = n // 10  #3
#         count += 1
#     return count
# print(count_number(257893))

# def count_number(n):
#     return len(str(n))
# print(count_number(254836123))

# import math
#
# def count_number(n):
#     return int(math.log10(n)) + 1
#
# print(count_number(24582221))


# for num in range(1, 101):
#     if num % 3 == 0 and num % 5 == 0:
#         print(num)

# user_input = input("Enter a number (or 'Quit' to exit): ")
# while True:
#     if user_input == 'Quit':
#         print('Exsting...')
#         break
#     else:
#         numbers = float(user_input)
#         if numbers > 0:
#             print("Positive Number: ", numbers)
#         elif numbers < 0:
#             print("Negative Number: ", numbers)
#         else:
#             print("Invalid Input")
#     user_input = input("Enter a number (or 'Quit' to exit): ")

# while True:
#     user_input = input("Enter a number (or 'Quit' to exit): ")
#
#     if user_input == 'Quit':
#         print("Exiting...")
#         break
#
#     try:
#         numbers = float(user_input)
#
#         if numbers > 0:
#             print("Positive Number:", numbers)
#         elif numbers < 0:
#             print("Negative Number:", numbers)
#         else:
#             print("Zero")
#     except ValueError:
#         print("Invalid Input, please enter a valid number.")


# def calculation(a, b, operation):
#     if operation == '+':
#         return a + b
#     elif operation == '-':
#         return  a - b
#     elif operation == '*':
#         return a * b
#     elif operation == '/':
#         return a / b
#     else:
#         print("Invalid Inputs")
# print(calculation(10, 25, '+'))

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n-1):
#         if n % i == 0:
#             return False
#     return True
# print(is_prime(2))

# guessed_number = 20
# attempts = 0
#
# while True:
#     user_input = int(input("Guess The your number: "))
#     attempts += 1
#
#     if user_input == guessed_number:
#         print("You are guessed write number")
#         print("Total attempts:", attempts)
#         break
#     elif user_input < guessed_number:
#         print("Too Low")
#     elif user_input > guessed_number:
#         print("Too High")
#     else:
#         print("Enter correct number")

# def twoSum(nums, target):
#     seen = {}  # stores number: index
#
#     for i, num in enumerate(nums):
#         diff = target - num  # the number we need
#
#         if diff in seen:     # if we already saw the matching number
#             return [seen[diff], i]
#
#         seen[num] = i        # store current number with index
#
# print(twoSum([2, 7, 11, 15], 9))

#Sets:-
s = {1,2,3,4,2,2,3}

# empty_set = set()
# print(type(empty_set))

print(s)

s.add(5)
print(s)

s.remove(5)
print(s)

s.clear()
print(s)

s1 = {1,2,3,4,5}
s2 = {1,3,2,2}

print(s1.union(s2))
print(s1.intersection(s2))