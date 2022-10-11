# use either when and/or if statements to solve below kotlin questions

# write a program to print the amount to be paid based on distance travelled

# distance                                                cost
# 0 through 100                                         5.00
# more than 100 but not more than 500                   8.00
# more than 500 but less than 1000                      10.00
# 1000 or more                                          12.00

dist = float(input("Enter distance travelled : "))

if dist <= 100 :
    print("cost : ",5.00 )
elif dist > 100 and dist <= 500:
    print("cost : ",8.00 )
elif dist > 500 and dist < 1000:
    print("cost : ",10.00 )
else :
    print("cost : ",12.00 )

# write a kotlin program to calculate total electricity bill to be paid based on units consumed according to thee given conditions

# usage                                                                 cost
# for first 50 units                                                     Rs. 0.50 per unit
# for the next 100 units                                                 Rs. 1.00 per unit
# for the next 100 units                                                 Rs. 1.20 per unit
# for units above 250                                                    Rs. 1.50 per unit

units = float(input("Enter you total units : "))

if units >= 0 and units <= 50 :
    total = units * 0.50
    print("Total : ",total)
elif units >= 51 and units <= 150 :
    total = units * 1.00
    print("Total : ",total)
elif units >= 151 and units <= 249 :
    total = units * 1.20
    print("Total : ",total)
else :
    total = units * 1.50
    print("Total : ",total)
