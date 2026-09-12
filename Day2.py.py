# Day 2 - Functions & Data Structures
# 1. List
students = ["Sayali","Sakshi","Priya","Gouri"]
print("Students:",students)
print("First Student:",
students[0])
print("Number of Students:",
len(students))

#Add a student
students.append("Aditi")
print("After Adding:", students)

#2 Tuple
marks=(60,80,90,83)

print("Marks:",marks)
print("First Mark:",marks[0])
print("Number of Marks:", len(marks))

#3.Dictionary
student={
    "name":"Sayali",
    "age":21,
    "course":"BCA",
    "marks":85
    }
print("Student Detaile:", student)
print("Name:", student["name"])
print("Course",
      student["course"])
print("marks", student["marks"])

#For Loop
print("Student Names:")
for name in students:print(name)

#Functions
def greet(name):
    print("Hello", name)
greet("Sayali")

#Functions With Calculation
def add_numbers(a,b):
    return a+b

result = add_numbers(20,10)
print("Addition:", result)
