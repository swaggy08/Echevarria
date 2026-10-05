from W9LA1Echevarriia import ECHEVARRIAcurrent

ECHEVARRIA1 = input(" Name: ")
ECHEVARRIA2 = ECHEVARRIA1.title()
print(f"Hello, {ECHEVARRIA1}!")

print("=== CALCULATION MENU ===")
print("1. Power")
print("2. Voltage")
print("3. Current")

ECHEVARRIA1 = int(input("Enter your choice: "))

if ECHEVARRIA1 == 1:
    ECHEVARRIAvoltage = int(input("Enter your voltage: (V): "))
    ECHEVARRIAcurrent = int(input("Enter your current: (C): "))
    ECHEVARRIApower = ECHEVARRIAvoltage * ECHEVARRIAcurrent
    print = ("Power = ", ECHEVARRIApower, "W")

elif ECHEVARRIA1 == 2:
    ECHEVARRIApower = int(input("Enter your power: (W): "))
    ECHEVARRIAcurrent = int(input("Enter your current: (A): "))
    ECHEVARRIAvoltage = ECHEVARRIApower / ECHEVARRIAcurrent
    print = ("Voltage= ", ECHEVARRIAvoltage, "V")

elif ECHEVARRIA1 == 3:
    ECHEVARRIApower = int(input("Enter your power: (W): "))
    ECHEVARRIAvoltage = int(input("Enter your voltage: (V): "))
    ECHEVARRIAcurrent = ECHEVARRIApower / ECHEVARRIAvoltage
    print = ("Current= ", ECHEVARRIAcurrent, "A ")

else:
    print("Invalid choices")




