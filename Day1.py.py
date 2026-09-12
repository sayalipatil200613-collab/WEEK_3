# Day 1- python basics
# 1.varible
name = "Sayali"
age = 21
marks = 85.00

print("Name:",name)
print("age:",age)
print("Marks:",marks)

# 2.Data Type
print(type(name))  #string
print(type(age))   #Integer
print(type(marks)) #Flot

#3.Operators
a=20
b=10
print("Addition:", a+b)
print("Subtraction:", a-b)
print("Multiplication:", a*b)
print("Division:", a/b)
print("Remainder:", a%b)

#4.control flow - If Else
if marks >=40:
    print("Result: Pass")
else:
    print("Result: Fail")

#For Loop
for i in range(1,5):
    print("Number:",i)
