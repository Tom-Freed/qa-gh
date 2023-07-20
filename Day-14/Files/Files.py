with open("teams.txt", "w") as file:
    teams = 'Chelsea\nLiverpool\nArsenal\nNewcastle\nManCity'
    file.write(teams)

with open("teams.txt", "r") as file:
    lines = file.readlines()
    print(lines[0].strip(), lines[3].strip())