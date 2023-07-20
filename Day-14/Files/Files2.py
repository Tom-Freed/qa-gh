with open("teams.txt", 'r') as file:
    content = file.read()

with open("teams.txt", 'w') as file:
    file.seek(0)
    file.write('This is a new line\n')
    file.write(content)