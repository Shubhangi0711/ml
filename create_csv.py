import csv

data = [
    ["Roll", "Name", "Marks" , "Grade" , "Age"],
    [1, "Rianka", 85 , "A", 20],
    [2, "Aman", 90 , "A+", 22],
    [3, "Shubhangi", 75, "B", 21],
    [4, "Nehal", 88 , "A", 20],
    [5, "Karun", 92 , "A+", 23]
]

with open("student.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV Created: student.csv")

with open("student.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)
    print("\nHeader:", header)

    print("\nData:")
    for row in reader:
        print(row)