# BMI calculator
# weight (KG)
# height (M)

# BMI = weight / (height ** 2)
# if < 18.5

name = str(input("Enter Your Name : "))
wt = float(input("Enter Your Weight (kg) : "))
ht = float(input("Enter Your Height (m) : "))

bmi = wt / (ht ** 2)

if bmi < 18.5 :
    print(name, "is UNDER-WEIGHT")
elif bmi >= 18.5 and bmi <= 22.9:
    print(name, "is NORMAL.")
elif bmi >= 23 and bmi <= 24.9:
    print(name, "is OVERWEIGHT.")
elif bmi >= 25 and bmi <= 29.9:
    print(name, "is PRE-OBESE.")
elif bmi >= 30 and bmi <= 34.9:
    print(name, "is OBESE CLASS I")
elif bmi >= 35 and bmi <= 39.9:
    print(name, "is OBESE CLASS II.")

else:
    print(name, " is OBESE CLASS III")