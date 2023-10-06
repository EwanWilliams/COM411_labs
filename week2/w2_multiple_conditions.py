def main():
    # ACTIVITY 1
    advType = input("Please enter the type of adventure you wish to embark upon: ")

    if advType == "scary" or advType =="short":
        print("Entering the dark forest!")
        # ACTIVITY 2
        sound = input("What did i hear? ")
        sight = input("What did i see? ")
        if sound == "grr" and sight == "two red eyes": print("There is a scary creature. I should get out of here!")
        else: print("I am a little scared but I will continue.")
    elif advType == "safe" or advType == "long":
        print("Taking the safe route!")
    else:
        print("Not sure which route to take.")


if __name__ == "__main__":
    main()