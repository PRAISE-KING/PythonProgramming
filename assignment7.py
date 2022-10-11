# write a code that will loop through a list of 10 counties in kenya ,then adds counties with two names
# inside a new list
# print a new list

counties = ["Bungoma","Kisumu","Mombasa","Nairobi","Kakamega","Uasin Gishu","Taita Taveta","Tana River","wajir","Nyandarua"]
print(len(counties))

newList = []

for county in counties:
    if " " in county:
        newList.append(county)
        print(newList)
        print(" ")

for county in counties:
    if " "not in county:
        newList.append(county)
        print(newList)