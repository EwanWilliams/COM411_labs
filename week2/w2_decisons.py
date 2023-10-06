def main():
    
    # ACTIVITY 1
    book = input("What type of book is this?\n")
    print(f"\nI like {book} books!\n\nFinished Reading Book.")


    # ACTIVITY 2
    activity = input("\nPlease enter the activity to be performed.\n")

    if activity == "calculate":
        print("\nPerforming calculations...\n")
    else:
        print("\nPerforming activity...\n")

    print("Activity completed")


    # ACTIVITY 3
    direction = input("\nTowards which direction should I go (up, down, left or right)?")

    if direction == "up": print("I am going up.")
    elif direction == "down": print("I am going down.")
    elif direction == "left": print("I am going left.")
    elif direction == "right": print("I am going right.")


    # ACTIVITY 4
    numCheck = int(input("\nPlease enter an integer: "))

    if numCheck % 2 == 0:
        print(f"{numCheck} is an even number.")
    else:
        print(f"{numCheck} is an odd number.")
    

    # ACTIVITY 5
    num1 = int(input("\nPlease enter the first number: "))
    num2 = int(input("Please enter the second number: "))

    if num1 < num2: print("The first number is smaller.")
    elif num2 < num1: print("The second number is smaller.")
    else: print("Both numbers are equal.")

    print()


    # ACTIVITY 6
    odds = 0
    evens = 0

    for i in range(3):
        numCheck2 = int(input("Please enter an integer: "))
        if numCheck2 % 2 == 0: evens += 1
        else: odds += 1
    
    print(f"There were {evens} evens and {odds} odds.")



if __name__ == "__main__":
    main()