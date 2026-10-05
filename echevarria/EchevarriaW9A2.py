print("GRADES")

EchevarriaName = input("Enter Name:  ")
EchevarriaItems = int(input("Enter Items:  "))
EchevarriaScore = int(input("Enter Score:  "))



EchevarriaAverage = EchevarriaScore / EchevarriaItems * 100


print("Score Percentage         Color")
print("90-96                 Light Green")
print("80-89                 Yellow Green")
print("70-79                     Yellow")
print("60-69                     Orange")
print("59 and below                Red")

if EchevarriaAverage >=97:
    print("Dark Green")
    print("PASSED")
elif EchevarriaAverage >= 90 and EchevarriaAverage <= 96:
 print("Light Green")
 print("PASSED")
elif EchevarriaAverage >= 80 and EchevarriaAverage <= 89:
 print("Yellow Green")
 print("PASSED")
elif EchevarriaAverage >= 70 and EchevarriaAverage <= 79:
 print("Yellow")
 print("PASSED")
elif EchevarriaAverage >= 60 and EchevarriaAverage <= 69:
 print("Orange")
 print("PASSED")

else:
 print("Red")
 print("FAILED")
print("==================================================")

print ("Your average score is:" , EchevarriaAverage )