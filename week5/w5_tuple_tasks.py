def main():
    run_task1()
    run_task2()
    run_task3()


#task 1
def run_task1():
    min_likelihood = likelihood()
    print(f"Minimum likelihood of falling: {min_likelihood}%")

def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    min_likelihood = likelihoods[0]

    for i in range(1, len(likelihoods), 1):
        if likelihoods[i] < min_likelihood:
            min_likelihood = likelihoods[i]

    return min_likelihood


#task 2
def run_task2():
    likelihoods = likelihood_min_max()
    print(f"Minimum likelihood of falling: {likelihoods[0]}%")
    print(f"Maximum likelihood of falling: {likelihoods[1]}%")

def likelihood_min_max():
    likelihoods = (50, 38, 27, 99, 4)
    min_likelihood = likelihoods[0]
    max_likelihood = likelihoods[0]

    for i in range(1, len(likelihoods), 1):
        if likelihoods[i] < min_likelihood:
            min_likelihood = likelihoods[i]
        if likelihoods[i] > max_likelihood:
            max_likelihood = likelihoods[i]
    
    return (min_likelihood, max_likelihood)
    

#task 3
def run_task3():
    steps_lst = steps()
    good_steps = []
    bad_steps = []

    for step in steps_lst:
        if step[1] >= 50:
            bad_steps.append(step)
        else:
            good_steps.append(step)
    
    print(f"Good steps: {len(good_steps)}, Bad steps: {len(bad_steps)}")

def steps():
    likelihoods = (("step 1", 50), ("step 2", 38), ("step 3", 27), ("step 4", 99), ("step 5", 4))
    return likelihoods



if __name__ == "__main__":
    main()
