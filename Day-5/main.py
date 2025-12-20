'''with open("names.txt", "w") as file:
    for i in range(5):
        name = input(f"Enter the Name: {i + 1}:")
        file.write(name + "\n")

with open("names.txt", "r") as file:
    print(file.read())'''

'''with open("log.txt", "a") as file:
    file.write("Program Run Successfully\n")

with open("log.txt", "r") as file:
    print("All Logs Below")
    print(file.read())'''

'''numbers = [5, 10, 15, 20, 25]
greater_number = [num for num in numbers if num > 15]
print(greater_number)'''

'''import json

# Step 1: Create 3 cities with populations
cities = {
    "Mumbai": 12442373,
    "Delhi": 11007835,
    "Pune": 3124458
}

# Step 2: Save the dictionary to cities.json
with open("cities.json", "w") as file:
    json.dump(cities, file, indent=4)

# Step 3: Read and display data from cities.json
with open("cities.json", "r") as file:
    data = json.load(file)

print("Cities and their populations:")
for city, population in data.items():
    print(f"{city}: {population}")

# Step 4: Ask user to add a new city
new_city = input("Enter a new city name: ")
new_population = input("Enter its population: ")

# Step 5: Update the dictionary and save again
data[new_city] = new_population

with open("cities.json", "w") as file:
    json.dump(data, file, indent=4)

print("New city added successfully!")'''


'''try:
    with open("data.txt", "r") as file:
        print(f"File is existed {file.read()}")
except FileNotFoundError:
    print("File is not found")'''
