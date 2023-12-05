import matplotlib.pyplot as plt
import random

def main():
    run_task1()
    run_task2()
    run_task3()
    run_task4()


#task 1
def run_task1():
    x_values = [1, 2, 3, 4, 5]
    y_values = [1, 4, 9, 16, 25]
    display_line(x_values, y_values)

def display_line(x, y):
    plt.plot(x,y)
    plt.savefig("task1.png")
    plt.close()


#task 2
def run_task2():
    small()
    medium()
    large()
    plt.savefig("task2.png")
    plt.close()

def small():
    x = [3, 4 ,4, 3, 3]
    y = [3, 3, 4, 4, 3]
    plt.plot(x, y, "ro:")

def medium():
    x = [2, 5, 5, 2, 2]
    y = [2, 2, 5, 5, 2]
    plt.plot(x, y, "gs--")

def large():
    x = [1, 6, 6, 1, 1]
    y = [1, 1, 6, 6, 1]
    plt.plot(x, y, "bp-")


#task 3
def run_task3():
    values = path()
    plt.plot(values[0], values[1])
    plt.savefig("task3.png")
    plt.close()

def coordinate():
    x = int(input("Enter x value: "))
    y = int(input("Enter y value: "))
    return (x, y)

def path():
    print("Retrieving path...")
    x_values = []
    y_values = []

    for i in range(4):
        data = coordinate()
        x_values.append(data[0])
        y_values.append(data[1])
    
    return [x_values, y_values]


#task 4
def run_task4():
    print("Running...")
    generate()
    print("Done!")

def data():
    paths = dict()
    paths["line"] = input("What type of line would you like : , -- or - ")
    paths["colour"] = input("What colour (r, g, b)? ")
    paths["marker"] = input("What marker style (o, s, ^)? ")
    return paths

def generate():
    num_lines = int(input("How many lines would you like to display? "))
    for i in range(num_lines):
        values = data()
        x = [random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,50)]
        y = [random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,50)]
        plt.plot(x, y, f"{values['colour']}{values['marker']}{values['line']}")
        plt.savefig(f"task4_{i}.png")
        plt.close()


if __name__ == "__main__":
    main()
