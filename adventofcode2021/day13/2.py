def main():
    cords = []
    folds = []
    with open('input.txt', 'r') as file:
        while line := file.readline():
            if line == "\n":
                continue
            if line[:-1].split()[0] != "fold":
                cords.append((int(line[:-1].split(",")[0]), int(line[:-1].split(",")[1]))) 
            else:
                folds.append((line.split()[2].split("=")[0], int(line.split()[2].split("=")[1])))

    temp = [x for x in cords]
    for f in folds:
        if f[0] == 'x':
            fold_horizontal(temp, f[1])
        else:
            fold_vertical(temp, f[1]) 
    show(temp)


def show(cords):
    columns = 0 
    rows = 0
    for c in cords:
        if c[0] > columns:
            columns = c[0]
        if c[1] > rows:
            rows = c[1]
    for y in range(rows+1):
        for x in range(columns+1):
            if (x, y) in cords:
                print("#", end="")
            else:
                print(" ", end="")
        print()

def fold_vertical(cords, row):
    temp = []
    for key, p in enumerate(cords):
        if p[1] == row:
            temp.append(p)
        if p[1] > row:
            location = row - (p[1] - row)
            check((p[0], location), cords)
            temp.append(p)
    for t in temp:
        cords.remove(t)
    return cords

def fold_horizontal(cords, column):
    temp = []
    for key, p in enumerate(cords):
        if p[0] == column:
            temp.append(p)
        if p[0] > column:
            location = column - (p[0] - column)
            check((location, p[1]), cords)
            temp.append(p)
    for t in temp:
        cords.remove(t)
    return cords

def check(position, cords):
    for p in cords:
        if position == p:
            return
    cords.append(position)
    return

main()
