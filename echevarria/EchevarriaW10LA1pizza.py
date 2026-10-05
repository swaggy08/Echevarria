Echevarriaflavor = input("Enter pizza flavor: ").lower()

match Echevarriaflavor:
    case "hawaiian":
        size = input("Enter size of pizza (small/medium/large): ").lower()

        match size:
            case "small":
                Echevarriaprice = 250
            case "medium":
                Echevarriaprice = 500
            case "large":
                Echevarriaprice = 1000
            case _:
                Echevarriaprice = 0
                print("Invalid size.")

    case "oreo":
        print("You selected oreo pizza")

        size = input("Enter size of pizza (small/medium/large): ").lower()

        match size:
            case "small":
                Echevarriaprice = 250
            case "medium":
                Echevarriaprice = 500
            case "large":
                Echevarriaprice = 1000
            case _:
                Echevarriaprice = 0
                print("Invalid size.")

    case _:
        Echevarriaprice = 0
        print("Invalid flavor.")

print("Total amount:", Echevarriaprice)
print("Flavor:", Echevarriaflavor)


