# Python dictionaries
# -holds a collection of keys with their values
# changeable , ordered , no duplicates allowed
# JSON file - dictionary (APIs) -JavaScript Object Notation
# created using braces {}

student = {
    "name" : "Praiz" ,
    "age" : 20 ,
    "course" : "cybersecurity" ,
    "gender" : "Male"
}

# operations
# accessing elements from a dictionary

print(student["name"])
print(student)

x = student.keys()
y = student.values()
z = student.items()

print(x)
print(y)
print(z)

student["height"] = 1.8
print(student)

student["course"] = "Software Engineering"
print(student)

student.pop("gender")
print(student)

