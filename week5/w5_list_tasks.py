def main():
    run_task1()
    run_task2()
    run_task3()
    run_task4()


#task 1
def run_task1():
    print(directions)

def directions():
    steps = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return steps


#task 2
def run_task2():
    print("Moving...")
    mov_list = movement()
    for i in range(0, len(mov_list), 2):
        print(f"{mov_list[i]} for {mov_list[i+1]} steps")
    
def movement():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path


#task 3
def run_task3():
    menu()

def menu():
    print("Please select a direction:")
    dir_list = directions()
    for i in range(len(dir_list)):
        print(f"{i}:{dir_list[i]}")


#task 4
def run_task4():
    route = []
    print("Working out escape route...")

    for i in range(5):
        route.append(menu_and_input())
    
    print(f"Escape route: {route}")

def menu_and_input():
    print("Please select a direction:")
    dir_list = directions()
    for i in range(len(dir_list)):
        print(f"{i}:{dir_list[i]}")
    
    usr_choice = int(input())
    return dir_list[usr_choice]


if __name__ == "__main__":
    main()
