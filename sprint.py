import random

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.brand} {self.model} {self.year}"

    def print_info(self):
        print("Car brand: " + self.brand)
        print("Car model: " + self.model)
        print("Car year: " + str(self.year))

class Lead:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"{self.name}"
    
    def print_info(self):
        print("name: " + self.name)

    def change_name(self, new_name):
        print("Old name is: " + self.name)
        self.name = new_name
        print("new name is: " + self.name)


class Student:
    def __init__(self, name, age, grades: list[float]):
        self.name = name
        self.age = age
        self.grades = grades
    
    def __str__(self):
        return f"Name: {self.name}, {self.age} years old, grades are: {self.grades}"
    
igor = Student("Igor", 28, [5.0, 4.85, 4.9])
bob = Student("Bob", 22, [5.0, 4.65, 5.0])
franklin = Student("Franklin", 26, [4.40, 4.95, 4.9])
murad = Student("Murad", 29, [4.0, 4.05, 4.1])
phil = Student("Phil", 27, [4.3, 3.65, 4.6])
arman = Student("Arman", 28, [4.80, 4.95, 4.9])

def get_avg_grades(student):
    avg = sum(i for i in student.grades)/len(student.grades)
    ##print(avg)
    return(avg)

st_list = [igor, bob, franklin, murad, phil, arman]
new_list = [i for i in st_list if get_avg_grades(i) > 4.1]

##for student in new_list:
##    print(student, ", average = ", round(get_avg_grades(student),2))

def weekday(i):
    match i:
        case 1:
            return 'Monday'
        case 2:
            return 'Tuesday'
        case 3:
            return 'Wendesday'
        case 4:
            return 'Thursday'
        case 5:
            return 'Friday'
        case 6:
            return 'Saturday'
        case 7:
            return 'Sunday'
        case _ :
            return 'Incorrect input number'
        
##i = int(input("Введите число от 1 до 7: "))
##print(weekday(i))

numbers = [random.randint(1,100) for i in range(9)]

max_num = numbers[0]
for i in numbers:
    if i > max_num:
        max_num = i
print(max_num)

while len(numbers) > 1:
    if numbers[0] > numbers[1]:
        numbers.pop(1)
    else:
        numbers.pop(0)
    ##print(numbers)

print(numbers[0])