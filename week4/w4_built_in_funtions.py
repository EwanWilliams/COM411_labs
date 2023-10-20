def main():
    #activity 1
    print("Program started!")
    char_1 = input("Please enter a standard character: ")
    
    if len(char_1) == 1:
        print(f"The ASCII code for {char_1} is {ord(char_1)}.")
    else:
        print("ERROR too many characters.")

    print("Program ended!")    


    #activity 2
    print("Program started!")
    ascii_1 = abs(int(input("Please enter an ASCII code: ")))

    if ascii_1 in range(32, 127):
        print(f"The character represented by the ASCII code {ascii_1} is {chr(ascii_1)}.")
    else:
        print("ERROR not in range.")

    print("Program ended!")


if __name__ == "__main__":
    main()
    