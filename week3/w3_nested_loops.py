def main():
    #ACTIVITY 1
    rows = int(input("How many rows should i have? "))
    cols = int(input("How many cols should i have? "))

    for i in range(rows):
        for j in range(cols):
            print(":) ", end="")
        print()
    print("Done!")
    
    #ACTIVITY 2
    sequence = input("Please enter a sequence: ")
    marker = input("Please enter the marker char: ")
    markerLoc1 = -1
    markerLoc2 = -1
    for i in range(len(sequence)):
        if sequence[i] == marker:
            if markerLoc1 == -1: markerLoc1 = i
            else: markerLoc2 = i
    print(f"The distance between the markers is: {markerLoc2 - markerLoc1 - 1}")


if __name__ == "__main__":
    main()