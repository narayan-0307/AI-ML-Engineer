'''
Create a class BankAccount with the following attributes:
        account_number, owner_name, balance

And add the following methods:
        deposit, withdraw and check_balance
'''
'''
class BankAccount:

    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited successfully")

    def withdraw (self, amount):
        if amount > self.balance:
            print("Insufficient Balance! ")
        else:
            self.balance -= amount
            print(f"{amount} withdraw successfully")

    def check_balance(self):
        print(f"Current Balance. {self.balance}")
'''
'''
Create a class Book with the following attributes:
                    title
                    author
                    list of reviews
And add methods to:
                    add a new review
                    count reviews
                    display all reviews
'''
'''
class Book:
    def __init__(self, title, author, list_of_reviews = None):
        self.title = title
        self.author = author
        self.list_of_reviews = list_of_reviews or []

    def add_review(self, addReview):
        self.list_of_reviews.append(addReview)
        print(f"Review added successfully: {addReview}")

    def count_reviews(self):
        print(f"Total Reviews: {len(self.list_of_reviews)}")

    def display_all_reviews(self):
        print("All Reviews:")
        for review in self.list_of_reviews:
            print(f"- {review}")
'''
'''
Encapsulation Concept:
Create a class Student with private attributes:
                                                _name
                                                _roll_no
                                                _marks

Provide getter and setter methods with validation, such as:
                        Marks cannot be negative
                        Roll number must be between 1 and 100
                        Name cannot be empty
'''
'''
class Student:
    def __init__(self, name, roll_no, marks):
        self.__name = name
        self.__roll_no = roll_no
        self.__marks = marks

    def get_name(self):
        return self.__name
    def get_roll_no(self):
        return self.__roll_no
    def get_marks(self):
        return self.__marks

    def set_name(self, name):
        if name == "":
            print("Name cannot be Empty!")
        else:
            self.__name = name
            print("Name updated successfully")
    def set_roll_no(self, roll_no):
        if roll_no < 1 or roll_no > 100:
            print("Roll number must be between 1 and 100")
        else:
            self.__roll_no = roll_no
            print("Roll updated successfully")

    def set_marks(self, marks):
        if marks < 0:
            print("Marks cannot be negative")
        else:
            self.__marks = marks
            print("Marks updated successfully")
'''
'''
* Inheritance: 
Create a base class Vehicle with attributes like brand and model.
Create two subclasses Car and Bike that add extra attributes — seats (in Car) & engine_cc (in Bike).
'''
'''
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc
'''

'''
* Abstraction
Create an abstract class Employee with an abstract method calculate_salary().
Create subclasses Intern, FullTimeEmployee, and ContractEmployee that implement the method differently.
'''
'''
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
class Intern(Employee):
    def calculate_salary(self):
        print("This is Intern calculator")

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        print("This is Full Time Employee calculator")

class ContractEmployee(Employee):
    def calculate_salary(self):
        print("This is Contract employee calculator")
'''

'''
Create a class Person that allows the constructor to work with:
• name only
• name + age
• name + age + address
Use default parameters to simulate constructor overloading.
'''
'''
class Person:
    def __init__(self, name, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")


p3 = Person("Ali")
p3.display_info()
'''
'''Create a class Player with:
• a class variable player_count
• instance variables name and level
Track how many players were created.'''

'''class Player:
    player_count = 0
    def __init__(self, name, level):
        self.name = name
        self.level = level
        Player.player_count += 1

    def show_player_count(self):
        print(f"Totol Players: {Player.player_count}")



player_1 = Player("Nobita Mestry", 1)

player_1.show_player_count()
'''

'''Create the following classes: Herbivore, Carnivore, Omnivore with some attributes & methods.
Then create a class Bear that inherits from all the above classes to showcase multiple inheritance.'''
'''class Herbivore:
    def __init__(self, chocolate):
        self.chocolate = chocolate

class Carnivore:
    def __init__(self, catberry):
        self.catberry = catberry

class Omnivore:
    def __init__(self, celebration_box):
        self.celebration_box = celebration_box

class Bear(Herbivore, Carnivore, Omnivore):
    def __init__(self, box, chocolate, catberry, celebration_box):
        super().__init__(chocolate)  # From Herbivore
        Carnivore.__init__(self, catberry)  # From Carnivore
        Omnivore.__init__(self, celebration_box)
        self.box = box

bear = Bear("Dark Fantacy", "5Star", "kitkat celebration box", "Gift Box")
print(bear.chocolate, bear.catberry, bear.celebration_box, bear.box)'''


'''class Message:
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content

    def display(self):
        print(f"{self.sender} : {self.content}")

class ChatRoom:
    def __init__(self):
        self.messages = []
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def broadcast(self, message):
        self.messages.append((message))
        message.display()

    def show_chat_history(self):
        print("\nChat History:")
        for msg in self.messages:
            msg.display()

class User:
    def __init__(self, username):
        self.username = username
        self.chatroom = None

    def join_room(self, chatroom):
        self.chatroom = chatroom
        self.add_user(self)
        print(f"{self.username} joined the chatroom")

    def leave_room(self):
        if self.chatroom:
            self.remove_user(self)
            print(f"{self.username} left the chatroom")
            self.chatroom = None
    def send_message(self, content):
        if self.chatroom:
            message = Message(self.username, content)
            self.chatroom.broadcast(message)
        else:
            print("You must join a chatroom before sending message")'''


'''class Book:
    def __init__(self, title, author, list_of_reviews=None):
        self.title = title
        self.author = author
        self.reviews_list = list_of_reviews or []

    def add_newReview(self, addReview):
        self.reviews_list.append(addReview)
        print(f"Review Added successfully: {addReview}")

    def count_reviews(self):
        # self.reviews_list.count(countReviews)
        # print(f"Total Reviews: {countReviews}")
        total = len(self.reviews_list)
        print(f"Total Reviews: {total}")
        return  total

    def get_all_reviews(self):
        # print(f"Our Reviews: {self.reviews_list}")
        print("All Reviews")
        for review in self.reviews_list:
            print("-", review)

addR = Book("It's Ok", "Jaya Kishori")
# addR.add_newReview("Reviews -1", "Nobita Mestry")
addR.add_newReview("Excellent Book")
addR.add_newReview("Very Helpful")


addR.count_reviews()
addR.get_all_reviews()'''


'''class Student:
    def __init__(self, name, roll_no, marks):
        self.__name = name
        self.__roll_no = roll_no
        self.__marks = marks

    # -----------------Getter function---------------------
    def get_name(self):
        return self.__name

    def get_roll_no(self):
        return self.__roll_no

    def get_marks(self):
        return self.__marks

    # -----------------Setter function---------------------
    def set_name(self, newName):
        if newName.stip() == "":
            print("Name can not be empty")
        else:
            self.__name = newName
            print(f"{newName} is updated successfully")

    def set_roll_no(self, set_rollNo):
        if set_rollNo < 0:
            print("Roll no can not be negative")
        elif set_rollNo < 1 or set_rollNo > 100:
            print("Roll number has to be between 1 & 100")
        else:
            self.__roll_no = set_rollNo
            print(f"{set_rollNo} is updated successfully")

    def set_marks(self, setMarks):
        if setMarks < 0:
            print("Marks cannot be negative")
        else:
            self.__marks = setMarks
            print(f"{setMarks} is updated successfully")'''

'''class Shape:
    def area(self):
        return "Area formula not defined"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius * self.radius)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height'''

'''class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc'''

'''from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Intern(Employee):
    def calculate_salary(self):
        print("This is 'Intern' calculation salary")

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        print("This is 'FullTimeEmployee' calculation salary function")

class ContractEmployee(Employee):
    def calculate_salary(self):
        print("This is 'ContactEmployee' calculation salary function")'''

'''class Persion:
    def __init__(self, name, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address

    def get_display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
p1 = Persion("Nobita Mestry")
p1.get_display()'''

'''class Player:
    player_count = 0

    def __init__(self, name, level):
        self.name = name
        self.level = level
        Player.player_count += 1

    def get_player(self):
        print(f"{self.name} : {self.level}")

    def show_player_count(self):
        print(f"The players were created: {self.player_count}")

p1 = Player("Nobita", "1")
p2 = Player("Shizuka", "2")
p3 = Player("Doreamon", "3")

p1.get_player()

p1.show_player_count()'''

class Herbivore:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print(f"The {self.name} : {self.age}")

'''class Carnivore:
    def __init__(self, game, level):
        self.game = game
        self.level = level

    def display_gamer(self):
        print(f"The game is: {self.game} & Level is: {self.level}")

class Omnivore:
    def __init__(self, instrument, skills):
        self.instrument = instrument
        self.skills = skills

    def display_musician(self):
        print(f"The is {self.instrument} instrument & my skills is: {self.skills}")

class Bear(Herbivore, Carnivore ,Omnivore):
    def __init__(self, name, age, game, level, instrument, skills):
        super().__init__(name, age)
        Carnivore.__init__(self, game, level)
        Omnivore.__init__(self, instrument, skills)

    def all_display(self):
        self.display_person()
        self.display_gamer()
        self.display_musician()
p = Bear("Nobita Mestry", 24, "Cricker", "5", "Casio", "Coder")
p.all_display()'''

#ChatRoom Class

class ChatRoom:
    def __init__(self, name):