import json

def main():
    run()
    run_task2()


#task 1
def run():
    read("futurama.json")

def read(file_path):
    with open(file_path) as f:
        data = json.load(f)
    
    print(f"Place Name: {data['location']}")
    print(f"Population Size: {data['population']}")

    for bot in data["bots"]:
        print(f"{bot['name']} has the following stats: {bot['stats']}")


#task 2
def run_task2():
    json_data = read_task2("futurama.json")
    save("exported.json", json_data)

def read_task2(file_path):
    print("Reading...")
    with open(file_path) as f:
        data = json.load(f)
    print("Done!")
    return data

def save(file_path, data):
    print("Exporting...")
    with open(file_path, "w") as f:
        json.dump(data, f, indent = 4)
    print("Done!")


if __name__ == "__main__":
    main()
