import csv

f = open("100 Sales Records.csv", 'rt')

reader = csv.reader(f)
counter = 0
total = 0
itemType = {}

next(f)
for row in reader:
     if row[0] == "Europe":
          counter+=1

     total+=int(row[8])
     itemType[row[2]] = row[3]


print("order records from Europe %d"%counter)
print("total amount of units sold %d"%total)

print ("list of item types:")
list = itemType.keys()
msg =""
for key in list:
   msg+=key + " "
print(list)
print(msg)


