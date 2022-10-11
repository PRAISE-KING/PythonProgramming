# Tuples Data type

# unchangeable , ordered , allow duplicates
# brackets ()
# single item in a tuple has a comma (,)

courses = ("android", "data science", "python")
language = ("python",)

# type

print(type(courses))
print(type(language))

# Accessing elements - ordered index , starts from zero ,[]

print(courses[1])
print(courses)

# incase you want to add e.g IOT then need to get back to list the n change then restore to tuple

x = list(courses)
print(x)

x.append("IOT")

courses = tuple(x)
print(courses)