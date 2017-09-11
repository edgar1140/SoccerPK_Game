def get_field():
    with open('players.txt', 'r') as file:
        text = file.read()
    return text


def get_teams():
    left = []
    with open('teams.txt', 'r') as file:
        file.readline()
        teams = file.readlines()
    for team in teams:
        split_string = team.strip().split(', ')
        left.append([
            split_string[0], split_string[1], split_string[2], split_string[3],
            split_string[4], split_string[5], split_string[6], split_string[7],
            split_string[8], split_string[9], split_string[10],
            split_string[11]
        ])
    return left