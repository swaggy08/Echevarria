students = {
    "ziggy" : 85,
    "ethan" : 90,
    "alonso" : 71,
    "mark" : 95
}
print("STUDENT GRADES:")
print("----------------")


students["bella"] = 75
students["karlo"] = 71
students["mae"] = 95
passing_grade = 75
name1 = input("Enter student name:")
grade1 = int(input("Enter grade:"))

students[name1] = grade1

print(students)
print("\nUpdate student grade")
print("-----------------------")

for name, grade in students.items():
    print(name, ":", grade)

search = input("\nEnter student name:")
if  search in students:
    print(search, "has a grade of", students[search])

else:
    print(search, "is not a student")
    highest = max(students, key=students.get)
    print(highest)
