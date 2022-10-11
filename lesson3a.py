# Data types
# 1).string, integer, float, boolean
# Arrays - a collectin of items together
# List , Tuple , Dictionary , Sets

# 1. List
# it contains a list of changeable, ordered, allow duplicates item
# items enclosed inside a squared brackets []

countries=["kenya","nigeria","uganda","somalia"]
numbers=[10,20,30,40]
instances=[True, False,False,True]

counties = [ "Nairobi" , 47 , "Mombasa" , 1 , True , 20.45]

# List operation
# 1. Length - len()

print(len(countries))

# 2.Type

print(type(countries))

# Accessing items in a list
# 1.Index - Starts from zero []

print(numbers[0])
print(countries[2])

# 2. range - first item is included , last item is excluded

print(countries[1:3])

fruits = [ "mango" , "banana" ,"watermelon" , "grapes" , "oranges" ,"apple" ]
# print out the third and the fourth element

print(fruits[2:4])

#  print the last element

print(fruits[5])

# Check the existence of an element (in)

if "banana" in fruits:
 print("banana exists")

if "melon" not in fruits :
    print("add melon")

# Adding , replacing an element , add list to a list
fruits.append("pineapple")
print(fruits)

# append() - adds a new element to a list

# Replacing element

fruits [1] = "mango"
print(fruits)

# fruits.insert(1 , "banana") adds ....
# print(fruits)

# extend() - adds list to list

fruits.extend(countries)
print(fruits)

# removing items from the list
# index - pop()

fruits.pop(8)
print(fruits)

# element - remove()

fruits.remove("apple")
print(fruits)

# Removing all the element - clear()

fruits.clear()
print(fruits)

del fruits
