'''data = True
line = 1
word = "Python"
with open("sample.txt", "r") as f:
    # content = f.read()
    # if "python" in content.lower():
    #     print("'Python' word is available")
    #     print(len(content))
    # else:
    #     print("'Python' word is not existed")
    while data:
        data = f.readline()
        if(word in data):
            print(f"{word} found at line {line}")
            break
        line += 1
        # print(data)'''

'''try:
    x = int(input("Enter the x: "))
    ans = 10 / x
except ZeroDivisionError:
    print("Divided by 0 is not allowed")
except ValueError:
    print("Invalid Input")
else:
    print(f"Answer: {ans}")
finally:
    print("End.....")'''

# numbers = [5, 10, 15, 20, 25]
# greater_number = [num for num in numbers if num > 15]
# print(greater_number)

'''labels = [ if num % 2 == 0 else "Odd number" for num in range(1, 6)]
print(labels)'''

'''Q1. File Write & Read
Create a Python program that:
Asks the user to enter 3 favorite movies
Writes each movie on a new line into a file named movies.txt
Opens the same file in read mode and prints all movies
'''
'''with open("movies.txt", "w") as file:
    for i in range(3):
        user_input = input(f"Enter the movie name {i + 1}: ")
        file.write(user_input + "\n")
with open("movies.txt", "r") as file:
    print(file.read())'''

'''Q2. Append Log with Date
Write a program that:
Opens a file system_log.txt in append mode
Appends a log entry like:
"System started at <current_time>"
Then reads and prints all log entries
(Hint: Use datetime module)'''

'''import datetime

with open("system_log.txt", "a") as file:
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write("System Started at:" + current_time)

with open("system_log.txt", "r") as file:
    print(file.read())'''

'''numbers = [3, 9, 12, 18, 21, 27]
new_number = [num for num in numbers if num % 3 == 0 and num > 15]
print(new_number)'''

'''import json

data = {
    "Amit": 88,
    "Riya": 92,
    "Sam": 75
}

with open("students.json", "w") as file:
    json.dump(data, file, indent=4)

print("Name & Marks")
with open("students.json", "r") as file:
    for name, marks in data.items():
        print(f"{name}: {marks}")

new_name = input("Enter the New Student name: ")
new_marks = int(input("Enter the it's marks: "))

data[new_name] = new_marks

with open("students.json", "w") as file:
    json.dump(data, file, indent=4)
'''

'''try:
    user_input = input("Enter a number: ")
    convert_integer = int(user_input)
    print(f"Square: {convert_integer * convert_integer}")
except ValueError:
    print("Invalid number!")'''