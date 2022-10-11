# Create a tuple of 5 schools
# add 3 more schools to the tuple

sch = ("TUM" , "Modcom" , "UOE" , "Butula" , "Miluki")
print(sch)

y = list(sch)

y.append("Kibabii")
y.append("Praizking Hill")
y.append("BG High")

sch = tuple(y)
print(sch)

