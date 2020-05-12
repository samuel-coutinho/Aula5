import csv

f = open("100 Sales Records.csv", 'rt')

reader = csv.reader(f)

csv_data = []
for row in reader:
     list = []
     list.append(row[0])
     list.append(row[1])
     list.append(row[13])
     csv_data.append(list)


with open('data.csv', 'w', newline="") as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csv_data)



