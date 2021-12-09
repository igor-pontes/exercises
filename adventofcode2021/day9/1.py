def main():
    heightmap = []
    with open('input.txt', 'r') as file:
        while line := file.readline()[0:-1]:
            heightmap.append([int(x) for x in line])
    risk_levels = []
    for key_h, h in enumerate(heightmap):
        for key_e, e in enumerate(h):
            if checkhorizontal(h, key_e) and checkvertical(heightmap, key_h, key_e):
                risk_levels.append(e+1)
    print(sum(risk_levels))

def checkvertical(heightmap, index_h, index_e):
    if index_h > 0 and index_h < len(heightmap)-1:
        if heightmap[index_h][index_e] < heightmap[index_h-1][index_e]:
            if heightmap[index_h][index_e] < heightmap[index_h+1][index_e]:
                return True
    else:
        if index_h == 0:
            if heightmap[index_h][index_e] < heightmap[index_h+1][index_e]:
                return True
        else:
            if heightmap[index_h][index_e] < heightmap[index_h-1][index_e]:
                return True
    return False

def checkhorizontal(line, index):
    if index > 0 and index < len(line)-1:
        if line[index-1] > line[index]:
            if line[index+1] > line[index]:
                return True
    else:
        if index == 0:
            if line[index+1] > line[index]:
                return True
        else:
            if line[index-1] > line[index]:
                return True
    return False

main()
