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
    temp = fold_horizontal(temp, 655)
    print(len(temp))

def fold_vertical(cords, row):
    temp = []
    for key, p in enumerate(cords):
        if p[1] == row:
            temp.append(key)
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
            temp.append(key)
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
