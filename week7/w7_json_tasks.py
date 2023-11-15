import json

def main():
    run()


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



if __name__ == "__main__":
    main()
