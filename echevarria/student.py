students = {
    "ziggy": [85],
    "ethan": [90],
    "alonso": [71],
    "mark": [95]
}

highest = 0
namehighest = ""
tally = 0
name75 = []

for name, grade in students.items():
    average = sum(grade) / len(grade)
    print(name, *grade, "Average", round(average, 2))

    if average > highest:
        highest = average
        namehighest = name

    for g in grade:
        if g < 75:
            tally += 1
            if name not in name75:
                name75.append(name)

print()
print("highest average is", round(highest, 2))
print(f"Congratulations, {namehighest}!")
print(f"There are {tally} grades below, owned by {','.join(name75)}")