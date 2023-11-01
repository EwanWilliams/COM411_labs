import csv

def main():
    run_task1()
    run_task2()
    run_task3()


#task 1
def run_task1():
    read_csv("clothing.csv")

def read_csv(path):
    with open(path) as f:
        reader = csv.reader(f)
        headings = next(reader)

        print(f"Headings:\n{headings}")
        print("Values:")

        for line in reader:
            print(line)


#task 2
def run_task2():
    extract("clothing.csv")

def extract(path):
    print("Extracting...")

    with open(path) as f:
        reader = csv.reader(f)
        headings = next(reader)
        names = ""
        
        for line in reader:
            names += f"{line[1]}\n"
        
        print("Done! The extracted items are as follows:")
        print(names.strip())


#task 3
def run_task3():
    export("exported_items.csv", 2)

def export(path, num_items):
    print("Exporting...")

    with open(path, "a") as f:
        for i in range(num_items):
            item_id = input("Enter item id: ")
            item_name = input("Enter item name: ")
            item_colour = input("Enter item colour: ")
            f.write(f"{item_id},{item_name},{item_colour}\n")
    
    print("Done!")


if __name__ == "__main__":
    main()