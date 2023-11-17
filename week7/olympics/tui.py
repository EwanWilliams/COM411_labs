def started(msg=""):
    print("-"*120)
    print(f"Operation started: {msg}...\n")


def completed():
    print("\nOperation completed.")
    print("-"*120)


def error(msg):
    print(f"Error! {msg}")


def menu():
    print(f"\nPlease select one of the following options:")
    print('''    [years]     List unique years
    [tally]     Tally up medals
    [ctally]    Tally up medals for each team
    [exit]      Exit the program
          ''')
    return input("Your selection: ")


def display_medal_tally(tally):
    print(f"| Gold       | {tally['Gold']:<11}|")
    print(f"| Silver     | {tally['Silver']:<11}|")
    print(f"| Bronze     | {tally['Bronze']:<11}|")


def display_team_medal_tally(team_tally):
    for team, medals in team_tally.items():
        print(f"{team}:")
        print(f"    Gold:{medals['Gold']}, Silver:{medals['Silver']}, Bronze:{medals['Bronze']}")


def display_years(years):
    for year in sorted(years,reverse=True):
        print(year)
