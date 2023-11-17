import csv
import process
import tui


def read_data(file_path):
    tui.started(f"Reading data from {file_path}")

    with open(file_path) as f:
        reader = csv.reader(f)
        next(reader)
        data = []
        line_list = []
        for line in reader:
            for value in line:
                line_list.append(value.strip('"'))
            data.append(line)
    
    tui.completed()
    return data


def run():
    athlete_data = read_data("athlete_events.csv")
    
    while True:
        selection = tui.menu()
        if selection == "years":
            tui.started("Listing years")
            tui.display_years(process.list_years(athlete_data))

        elif selection == "tally":
            tui.started("Tallying medals")
            tui.display_medal_tally(process.tally_medals(athlete_data))

        elif selection == "team":
            tui.started("Tallying medals for each team")
            tui.display_team_medal_tally(process.tally_team_medals(athlete_data))

        elif selection == "exit":
            break
        else:
            tui.error("Invalid Selection!")
        
        tui.completed()


if __name__ == "__main__":
    run()
