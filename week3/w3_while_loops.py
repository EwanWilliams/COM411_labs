def main():
    #ACTIVITY 1
    appleNum = int(input("How many apples should I remove? "))
    remApple = 0
    while remApple < appleNum:
        print("Removed apple.")
        remApple += 1
    
    #ACTIVITY 2
    obstacles = int(input("How many obstacles must I avoid? "))
    obsAvoid = 0
    while obsAvoid < obstacles:
        print("Avoiding...", end="")
        obsAvoid += 1
        print(f"Done! {obsAvoid} obstacles avoided.")
    print("All obstacles have been avoided.")

    #ACTIVITY 3
    bars = int(input("How many bars should be charged? "))
    chargedBars = 0
    while chargedBars < bars:
        chargedBars += 1
        print("Charging: " + "█" * chargedBars)
    print("The battery is fully charged.")

    #ACTIVITY 4
    phrase = len(input("Please enter a phrase: "))
    print("Hi " * phrase)

    #ACTIVITY 5
    print("Calculating the sum of the first 100 numbers...")
    i = 1
    total = 0
    while i <= 100:
        total += i
        i += 1
    print(f"...done! The answer is {total}.")

    #ACTIVITY 6
    numSum = int(input("How many numbers should I sum up? "))
    i = 0
    total = 0
    while i < numSum:
        newNum = int(input(f"Please enter number {i+1} of {numSum}: "))
        total += newNum
        i += 1
    print(f"The answer is: {total}.")


if __name__ == "__main__":
    main()