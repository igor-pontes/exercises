flashes = 0
directions = {(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)}
octopodes = []
def main(steps):
    global octopodes, flashes
    with open('input.txt', 'r') as file:
        while line := file.readline():
            octopodes.append([int(x) for x in line[:-1]])
    s = 0
    while True:
        s += 1
        step(octopodes)
        if check(octopodes):
            print(s)
            break
        

def check(octopodes):
    visited = []
    for row in range(len(octopodes)):
        for column in range(len(octopodes[row])):
            flash((row, column), visited, False)
            if len(visited) == 100:
                return True

def flash(position, visited, increment):
    global flashes, octopodes, directions
    if position in visited:
        return False
    row = position[0]
    column = position[1]
    if row < 0 or row > 9:
        return False
    if column < 0 or column > 9:
        return False
    if increment:
        octopodes[row][column] += 1
    if octopodes[row][column] > 9:
        flashes += 1
        octopodes[row][column] = 0
        visited.append(position)
        for d in directions:
            flash(tuple(map(lambda i, j: i + j, position, d)), visited, True)
        return True
    else:
        return False

def step(octopodes):
    for row in range(len(octopodes)):
        for column in range(len(octopodes[row])):
            octopodes[row][column] += 1

main(100)
