def main():
    run_task1()
    run_task2()
    run_task3()


#task 1
def run_task1():
    print(observed())

def observed():
    observations = {"Car", "Sky Scraper", "Sky Scraper", "Bike", "House", "House"}
    return observations


#task 2
def run_task2():
    print("Counting observations...")
    obs_list = observed_items_task2()
    obs_set = set()

    for item in obs_list:
        obs_set.add((item, obs_list.count(item)))
    
    for value in obs_set:
        print(f"{value[0]} was observed {value[1]} times.")

def observed_items_task2():
    observations = []
    for i in range(7):
        observations.append(input("Please enter an observation: "))
    return observations


#task 3
def run_task3():
    obs_list = observed_items_task3()
    obs_list = remove_observations(obs_list)
    obs_set = set()

    for item in obs_list:
        obs_set.add((item, obs_list.count(item)))
    
    obs_set = sorted(obs_set)

    for value in obs_set:
        print(f"{value[0]} was observed {value[1]} times.")


def observed_items_task3():
    observations = []
    for i in range(5):
        observations.append(input("Please enter an observation: "))
    return observations

def remove_observations(obs_list):
    while input("Do you wish to remove an observation (y/n)?") == "y":
        rem_value = input("What observation do you wish to remove? ")
        obs_list.remove(rem_value)
    return obs_list


if __name__ == "__main__":
    main()
    