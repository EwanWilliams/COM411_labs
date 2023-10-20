import random as rnd

def main():
    play_guess_the_number()

def play_guess_the_number():
    #activity 1
    min_num = int(input("Please enter the minumum value: "))
    max_num = int(input("Please enterh the maxumum value: "))
    random_num = rnd.randrange(min_num, max_num, 1)

    print(f"I'm thinking of a number between {min_num} and {max_num}. Can you guess what it is?")
    while 1:
        guess = int(input("Enter guess: "))
        if guess > random_num:
            print("Your guess is too high.")
        elif guess < random_num:
            print("Your guess is too low.")
        elif guess == random_num:
            break
        print("Try again!")
    print("Congratulations! You guessed my number!")



if __name__ == "__main__":
    main()
