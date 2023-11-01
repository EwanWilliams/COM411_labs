import csv
headings = []
records = []

def run():
    load_data("titanic.csv")
    print(f"Successfully loaded {len(records)} records.")

    selected_option = display_menu()
    print(f"You have selected option: {selected_option}")

    if selected_option == 1:
        display_passenger_names()
    elif selected_option == 2:
        display_num_survivors()
    elif selected_option == 3:
        display_passengers_per_gender()
    elif selected_option == 4:
        display_passengers_per_age_group()
    elif selected_option == 5:
        display_survivors_per_age_group()
    else:
        print("Error! Option not recognised!")


#task 1
def load_data(file_path):
    print("Loading data...")

    with open(file_path) as f:
        reader = csv.reader(f)
        headings.append(next(reader))

        for line in reader:
            records.append(line)
    
    print("Done!")


#task 2
def display_menu():
    print("""
Please select one of the following options:
  [1] Display the names of all passengers
  [2] Display the number of passengers that survived
  [3] Display the number of passengers per gender
  [4] Display the number of passengers per age group
  [5] Display the number of survivors per age group
"""
    )
    return int(input("Enter selection: "))


#task 3
def display_passenger_names():
    print("The names of the passengers are...")

    for entry in records:
        print(entry[3])


#task 4
def display_num_survivors():
    num_survived = 0

    for entry in records:
        if int(entry[1]) == True:
            num_survived += 1
    
    print(f"{num_survived} passengers survived")


#task 5
def display_passengers_per_gender():
    females = 0
    males = 0

    for entry in records:
        if entry[4] == "female": females += 1
        elif entry[4] == "male": males += 1
    
    print(f"females: {females}, males: {males}")


#task 6
def display_passengers_per_age_group():
    children = 0
    adults = 0
    elderly = 0

    for entry in records:
        if entry[5] == "":
            continue
        elif float(entry[5]) < 18:
            children += 1
        elif float(entry[5]) < 65:
            adults += 1
        else:
            elderly += 1
    
    print(f"children: {children}, adults: {adults}, elderly: {elderly}")


#task 7
def display_survivors_per_age_group():
    children = 0
    survived_children = 0
    adults = 0
    survived_adults = 0
    elderly = 0
    survived_elderly = 0

    for entry in records:
        if entry[5] == "": continue
        elif float(entry[5]) < 18:
            children += 1
            if int(entry[1]) == True: survived_children += 1
        elif float(entry[5]) < 65:
            adults += 1
            if int(entry[1]) == True: survived_adults += 1
        else:
            elderly += 1
            if int(entry[1]) == True: survived_elderly += 1

    print(f"children: {survived_children}/{children}, adults: {survived_adults}/{adults}, elderly: {survived_elderly}/{elderly}")
    

if __name__ == "__main__":
    run()
