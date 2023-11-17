def list_years(data):
    years = set()

    for entry in data:
        years.add(entry[9])

    return years


def tally_medals(data):
    medals = {"Gold":0, "Silver":0, "Bronze":0}

    for entry in data:
        if entry[14] == "NA": continue
        medals[entry[14]] += 1

    return medals


def tally_team_medals(data):
    team_medals = dict()

    for entry in data:
        if entry[14] == "NA": continue
        try:
            team_medals[entry[6]][entry[14]] += 1
        except:
            team_medals.update({entry[6]: {"Gold":0, "Silver":0, "Bronze":0}})
            team_medals[entry[6]][entry[14]] += 1
    
    return team_medals
