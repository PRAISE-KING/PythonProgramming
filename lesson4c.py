# 3). if..elif...else

# Grading System Logical Operators
# 0-40 - D
# 41-55 - C
# 56-69 - B
# 70 and above - A upto 100
# Below 40 - Did not meet the passmark
# above 100 , less than 0 - invalid marks

marks = int(input("Enter Your Marks: "))

if marks > 0 and marks <= 40:
    print("Your Score is D.")
elif marks > 40 and marks <= 55:
    print("Your Score is C.")
elif marks >=56 and marks <= 69:
    print("Your Score is B.")
elif marks >=70 and marks <= 100:
    print("Your Score is A.")

else:
    print("Invalid Marks.")