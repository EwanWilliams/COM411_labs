def main():
    #activity 1

    name = input("What is your name? ")
    print(f"It is nice to meet you {name}")

    
    #activity 2

    eye = input("Please enter a character for your robot's eyes: ")
    print("##########")
    print(f"#  {eye}   {eye} #")
    print("#   ___  #")
    print("##########")


    #activity 3

    age = int(input("Please enter your age in years: "))
    height = float(input("Please enter your height in metres: "))
    mass = int(input("Please enter your mass in kg: "))

    bmi = round(mass/height**2, 3)

    print(f"{name} you are {age} years old and your BMI is {bmi}\n")


    #activity 4

    lives = int(input("Please enter the number of lives: "))
    energy = int(input("Please enter the energy level: "))
    shield = int(input("Please enter the shield level: "))

    print("Lives:", "♥"*lives)
    print("Energy:", "♦"*energy)
    print("Shield:", "♦"*shield)




if __name__ == "__main__":
    main()