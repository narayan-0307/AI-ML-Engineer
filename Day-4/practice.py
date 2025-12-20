'''
Product store
Design & create an online store for Products (name, price).
Track total products being created.
Create a static method to calculate discount on each product based on a % parameter.
'''
'''
class Product:

    count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1

    def get_info(self):
        print(f"Price of {self.name} is Rs.{self.price}")

    def get_count(cls):
        print(f"Total products in store: {cls.count}")

    @staticmethod
    def calculate_discount(price, discount):
        print(f"Discount price is: {price - (price * discount / 100)}")

product_1 = Product("Samsung Phone", 15_000)
product_2 = Product("Laptop", 50_000)
product_3 = Product("Pen", 10)

product_1.get_count()
product_2.calculate_discount(product_2.price, 25)
'''
'''
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    #Getter
    def get_balance(self):
        return self.__balance

    #Setter
    def set_balance(self,newBalance):
        self.__balance = newBalance

acc1 = BankAccount("Nobita Mestry", 100_000)
# acc1.set_balance(200_000)
# print(acc1.get_balance())

print(acc1.name, acc1._BankAccount__balance)
'''

#Inheritance: Multi lavel inheritahce
'''
class Employee:
    start_time = "10am"
    end_time = "6pm"

class AdminStaff(Employee):
    def __init__(self, role):
        self.role = role

class Accountant(AdminStaff):
    def __init__(self, salary, role):
        super().__init__(role)
        self.salary = salary
acc1 = Accountant(25_000, "CA")
print(acc1.role, acc1.salary, acc1.start_time, acc1.end_time)
'''

'''class Student:
    subject = "Python"
    college = "ABC"
    year = "4th year"
# students = []#
# for i in range(1, 3001):
#     s = Student()
#     students.append(s)#
# print(len(students))
stud1 = Student()
print(stud1.subject, stud1.college, stud1.year)'''

class Product:
    count = 0
    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1

    def get_info(self):
        print(f"Price of '{self.name}' is 'Rs.{self.price}'")

    @classmethod
    def get_count(cls):
        print(f"Total Products in store: {cls.count}")

    @staticmethod
    def cal_discount(price, discount):
        print(f"Final Discount is: {price - (discount * price) / 100}")

p1 = Product("Phone", 10_000)
p1 = Product("Laptop", 40_000)
p3 = Product("Pen", 10)

p1.get_info()

Product.get_count()

p1.cal_discount(p1.price, 12)