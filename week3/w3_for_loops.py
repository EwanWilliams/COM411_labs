def main():
    #ACTIVITY 1
    for i in range(int(input("How many mountains should I display? "))):
        if i == 0: print("Displaying...")
        print("           __\n          /  \_ \n         /^    \ \n        /  ^    \_\n      _/ ^ ^     ^\ \n     /  ^     ^    \ ")
    print("Done!")

    #ACTIVITY 2
    for i in range(int(input("How far are we from the target? ")), 0, -1):
        print(f"{i} steps remaining.")
    print("Target achieved!")

    #ACTIVITY 3
    for i in range(2, int(input("What level of brightness is required? ")) + 1, 2):
        if i == 2: print("Adjusting brightness...")
        print("Brightness level: " + "*" * i)
    print("Complete!")

    #ACTIVITY 4
    word = input("What word do you see? ")
    print("Displaying index positions...")
    for i in range(len(word)):
        print(f"index {i}: {word[i]}")
    print("Done!")

    #ACTIVITY 5
    phrase = input("What phrase would you like to see in reverse? ")
    print("Reversing...\nThe phrase is: ", end="")
    for i in range(len(phrase) - 1, -1, -1):
        print(phrase[i], end="")
    print()

    #ACTIVITY 6
    phrase = input("What phrase do you see? ")
    print("The phrase is:")
    for letter in phrase:
        print(letter)

    


if __name__ == "__main__":
    main()