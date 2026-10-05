patients = { "ziggy": (105, 130, 400),
             "alex": (80,90,100) }


normal = 120
for pn, bs in patients.items():
    if (pn == "rhea"):
        print("rhea")
        print("blood sugar summary")
        for value in bs:
            if value < 120:
                print(value, "not normal")

            else:
                print(value, "normal")

        highest = max(bs)
        print("highest blood sugar summary")
        lowest = min(bs)
        diff = highest - lowest
        print(diff)


