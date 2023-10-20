def main():
    listen()
    identify()
    escape_by("jumping over")
    escape_by("running around")
    escape_by("cross the bridge ahead")
    cross_bridge(3)
    cross_bridge(6)
    climb_ladder(5, 2)
    climb_ladder(2, 5)
    create_ladder()
    run()
    map_found()


def listen():
    sound = input("What do you hear? ")
    print(f"That was a loud {sound}!")


def identify():
    sight = input("What do you see? ")
    if sight == "a large boulder":
        print("It's time to run!")
    else:
        print("We will be fine.")


def escape_by(plan):
    if plan == "jumping over":
        print("We cannot escape that way! The boulder is moving too fast!")
    elif plan == "cross the bridge ahead":
        print("That might just work! Let's go!")
    else:
        print("We cannot escape that way! The boulder is in the way!")


def cross_bridge(steps):
    for i in range(steps):
        print("Crossed step.")
    if steps < 5:
        print("We must keep going!")
    else:
        print("The bridge is collapsing!")


def climb_ladder(remain, crossed):
    if remain > crossed:
        print("Still some way to go!")
    else:
        print("We are almost there!")


def display_ladder(steps):
    print("| |")
    for i in range(steps):
        print("---")
        print("| |")

def create_ladder():
    steps = int(input("Enter number of steps: "))
    display_ladder(steps)


def sum_weights(char_w, invent_w):
    return char_w + invent_w

def calc_avg_weight(char_w, invent_w):
    return sum_weights(char_w, invent_w)/2

def run():
    char_w = int(input("Enter character weight: "))
    invent_w = int(input("Enter inventory weight: "))
    choice = input("Enter 'sum' or 'average': ")
    if choice == "sum":
        print(f"Total weight: {sum_weights(char_w, invent_w)}")
    elif choice == "average":
        print(f"Average weight: {calc_avg_weight(char_w, invent_w)}")
    

def map_found():
    word = input("Enter a word: ")
    print("1) Dipslay in a box")
    print("2) Display lower-case")
    print("3) Display upper-case")
    print("4) Display mirrored")
    print("5) Repeat")
    choice = int(input("Enter choice: "))

    if choice == 1:
        display_box(word)
    elif choice == 2:
        display_lower(word)
    elif choice == 3:
        display_upper(word)
    elif choice == 4:
        display_mirror(word)
    elif choice == 5:
        repeat(word)

def display_box(word):
    print(" ", end="")
    print("_"*len(word))
    print("|" + " "*len(word) + "|") 
    print(f"|{word}|")
    print("|" + "_"*(len(word)) + "|")

def display_lower(word):
    print(word.lower())

def display_upper(word):
    print(word.upper())

def display_mirror(word):
    for i in range(len(word)-1, -1, -1):
        print(word[i], end="")
    print()

def repeat(word):
    repeats = int(input("How many repeats? "))
    for i in range(repeats):
        if i % 2 == 0:
            print(word.lower())
        else:
            print(word.upper())



if __name__ == "__main__":
    main()