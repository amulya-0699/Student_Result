import matplotlib.pyplot as pt

# Student 1
name1 = input("Enter Student Name : ")
roll1 = int(input("Enter Roll No. : "))

mark1 = []

for i in range(5):
    mark = float(input(f"Enter Marks of M{i+1}: "))
    mark1.append(mark)

total1 = sum(mark1)
per1 = total1 / 5.0

# Student 2
name2 = input("Enter Student Name : ")
roll2 = int(input("Enter Roll No. : "))

mark2 = []

for i in range(5):
    mark = float(input(f"Enter Marks of M{i+1}: "))
    mark2.append(mark)

total2 = sum(mark2)
per2 = total2 / 5.0

# Subjects
x = ["M1", "M2", "M3", "M4", "M5"]

y1 = mark1
y2 = mark2

# Plot graph
pt.plot(x, y1, marker="o", label=name1)
pt.plot(x, y2, marker="o", label=name2)

pt.title("Student Result Comparison")
pt.xlabel("Subjects")
pt.ylabel("Marks")

pt.legend()
pt.grid(True)

pt.show()