def main():
    # ACTIVITY 1
    book = input("What type of cover does the book have? ")

    if book == "soft":
        perfectBound = input("Is the book perfect bound? ")
        if perfectBound == "yes":
            print("Soft cover, perfect bound books are very popular!")
        else:
            print("Soft covers with coils or stitches are great for short books.")
    elif book == "hard":
        print("Books with hard covers can be more expensive!")
    

    # ACTIVITY 2
    checkLoc = input("Where should i look? ")

    if checkLoc == "in the bedroom":
        checkLoc = input("Where in the bedroom should i look? ")
        if checkLoc == "under the bed": print("Found some shoes but no phone.")
        else: print("Found some mess but no phone.")
    elif checkLoc == "in the bathroom":
        checkLoc = input("Where in the bathroom should i look? ")
        if checkLoc == "in the bathtub": print("Found a rubber duck but no phone.")
        else: print("Found bathroom stuff but no phone.")
    elif checkLoc == "in the living room":
        checkLoc = input("Where in the living room should i look? ")
        if checkLoc == "on the table": print("Yes! I found my phone!")
        else: print("Found some stuff but no phone.")



if __name__ == "__main__":
    main()