'''
Given a list of tuples with info(name, object):
    list all unique course
    list students enrolled in English
    create dictionary (student, set of courses)
'''

# info = [
#     ("Alice", "Math"),
#     ("Bob", "Science"),
#     ("Alice", "Science"),
#     ("Charlie", "Math"),
#     ("Bob", "Math"),
#     ("Alice", "English"),
#     ("Charlie", "English"),
# ]

#1 List all unique courses:

# courses_set = set()
# for tup in info:
#     # print(tup[0]) #NAMES
#     courses_set.add((tup[1])) #COURSES

# for names, courses in info:
#     # print(names, courses)
#     courses_set.add(courses)
#
# print(courses_set)

#2 List students enrolled in English:
# for name, course in info:
#     if (course == "English"):
#         print(name)

#3. create dictionary (student, set of courses)
# dict_courses = {}
#
# for name, course in info:
#     if (dict_courses.get(name) == None):
#         dict_courses.update({name: set()})
#         dict_courses[name].add(course)
#     else:
#         dict_courses[name].add(course)
#
# print(dict_courses)


#Q.1 Ask the user for string a check wheather it is a palindrome or not.
'''
def is_palindrome(text):
    text_lower = text.lower()
    text_clean = text_lower.replace(" ", "")  # remove spaces
    return text_clean == text_clean[::-1]     # compare with reverse


user_words = input("Enter the words: ")
if is_palindrome(user_words):
    print(f"{user_words} is a palindrome")
else:
    print(f"{user_words} is not a palindrome")
'''

#Q.2 List of integer compute the average of all number in the list

'''
list = [2,4,6,8,9]
total = 0
count = 0
for num in list:
    total += num
    count += 1
average = total / count
print(f"The average of {average}")

Answer - 2
numbers = [2,4,6,8,9]
totol = sum(numbers)
count = len(numbers)
average = totol / count
print(f"The average is: {average}")
'''

#Q.3 Input two lists of integer from the user. Merge them into one list and sort the result
'''

list1 = [1,2,7]
list2 = [2,4,5]

print("____________Merged List______________")
merged_list = list1 + list2
print(merged_list)

print("____________Sorted List______________")
merged_list.sort()
print(merged_list)

'''

#Tuple of integers: 1.All even numbers 2.All odd numbers
'''
my_tup = (1,2,3,4,5,6)
even_tup = ()
odd_tup = ()
for num in my_tup:
    if num % 2 == 0:
        even_tup += (num,)
    else:
        odd_tup += (num,)
print("Even Numbers tuple: ",even_tup)
print("Odd Numbers tuple: ",odd_tup)
'''

'''
Question-4 :
Create a dictionary where:

Keys = student names

Values = marks (integer)

Then write a menu-based program where the user presses:

A → Add a student

B → Update marks

C → Search for a student

D → Display all students & marks
'''
'''
students = {
    "Nobita": 85,
    "Shizuka": 92,
    "Doreamon": 78,
    "Gian": 88,
    "Sunio": 95
}
while True:
    print("A - Add a Student")
    print("B - Update Marks")
    print("C - Search for a student")
    print("D - Display all students and marks")
    print("E - Exit")

    choice = input("Enter your choice (A/B/C/D/E): ").upper()

    #Add a student:
    if choice == "A":
            name = input("Enter student name: ")
            marks = int(input("Enter the student marks: "))
            students[name] = marks
            print("Student Successfully Added")
            print(students)

    #Update a Marks:
    elif choice == "B":
        name = input("Enter the student to update marks: ")
        if name in students:
            new_marks = int(input("Enter the new marks: "))
            students[name] = new_marks
            print(students)
        else:
            print("Student not found")

    #Search for a student
    elif choice == "C":
        name = input("Enter a student name to search: ")
        for name, marks in students:
            print(f"{name}'s marks: {marks}")

    #Display all the students
    elif choice == "D":
        for name, marks in students.items():
            print(f"{name} : {marks}")

    #Exit
    elif choice == "E":
        print("Exsting Program.....")
        break

    else:
        print("Invalid choice! Please choose A, B, C, D or E.")
'''

#Question - 6: Dictionary map each words
'''
words = ["apple", "banana", "kiwi", "cherry", "mango"]

convert_dict = {}

for word in words:
    convert_dict[word] = len(word)

print(convert_dict)
'''

#takes a String -> from user -> print number of spaces in string
'''
my_string = input("Enter the String: ")

count = 0

for ch in my_string:
    if ch == " ":
        count += 1

print("Total Space: ", count)
'''

#Write a program to check whether two lists share no common elements.
'''
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

convert_set1 = set(list1)
print(convert_set1)

convert_set2 = set(list2)
print(convert_set2)

common_element = convert_set1.intersection(convert_set2)
if common_element:
    print("Commom elements", common_element)
else:
    print("No Common Element")
'''

#Given a list, print all elements that appear more than once in the list.
'''
list = [1, 2, 3, 2, 4, 5, 3, 6, 2]

duplicates = set()

for num in list:
    if list.count(num) > 1:
        duplicates.add(num)

print("Duplicates Elements: ", duplicates)
'''

'''
#“Ask the user for a string and print:
        1. All unique characters
        2. The count of unique characters”*
'''

user_input = input("Enter the string: ")

unique_chars = set(user_input)

print("Unique characters:", unique_chars)
print("Count of unique characters:", len(unique_chars))


