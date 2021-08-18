import csv

#Add your code here
data = csv.DictReader(open("Sample1.csv"))
print("CSV file as a dictionary:\n")
for row in data:
   print(row)
