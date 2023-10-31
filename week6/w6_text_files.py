import os

def main():
    run_task1()
    run_task2()
    run_task3()
    run_task4()


#task 1
def run_task1():
    print("Processing...")
    cwd()

def cwd():
    path = os.getcwd()
    print(f"The current working directory is {path}")

    print("The directory contains the following files:")
    for file in os.listdir(path):
        print(file)


#task 2
def run_task2():
    display_chars("library.txt", 5)
    display_line("library.txt")
    display_text("library.txt")

def display_chars(path, num_char):
    print(f"The first {num_char} characters are: ")
    with open(path) as f:
        print(f.read(num_char))

def display_line(path):
    with open(path) as f:
        print(f.readline())

def display_text(path):
    with open(path) as f:
        print(f.read())


#task 3
def run_task3():
    search("library.txt")

def search(filename):
    print("Searching...")
    with open(filename) as f:
        for line in f:
            print(f"Looked in {line.strip()}")
    print("...done!")


#task 4
def run_task4():
    data = search_books("books.txt")
    save("section-books.txt", data)

def search_books(path):
    print("Searching...", end="")
    sections = ""
    books = "Books:\n"

    with open(path, "r") as f:
        for line in f:
            if line.startswith("Section") == True:
                sections += line
            else:
                books += line
    
    print("Done!")
    return f"{sections}\n\n{books}"

def save(path, data):
    print("Saving...", end="")
    with open(path, "w") as f:
        f.write(data)
    print("Done!")



if __name__ == "__main__":
    main()
