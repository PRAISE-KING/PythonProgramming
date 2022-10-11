# sequencial
# decisional
# repetitions - a block (group) of code is repeated based on conditions - loops
# for loop
# while loop

# for

name = "MODCOM"
for check in name:
    print(check)

# a list
countries = ["Kenya","South Africa","Somalia","Tanzania","Uganda"]
for country in countries:
    print(country)
# loops using range functions
for count in range(10):
    print(count)
print(" ")
for count in range(3,10):
    print(count)

countries = ["Kenya","South Africa","Somalia","Tanzania","Uganda"]
for country in countries:
    print(country)
    if country == "Somalia":
        break
    print(country)
print(" ")

countries = ["Kenya", "South Africa", "Somalia", "Tanzania", "Uganda"]
for country in countries:
    print(country)
    if country == "South Africa":
        continue
    print(country)
print(" ")
# break - Terminates the loop if the condition is reached (counts upto)
# continue skips an items

# loops using range function
# range - start, limit, increament

for count in range(3, 10 , 2):
    print(count)

