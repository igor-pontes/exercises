from functools import reduce
def main():
    heightmap = []
    with open('input.txt', 'r') as file:
        while line := file.readline()[0:-1]:
            heightmap.append([int(x) for x in line])
    risk_levels = []
    basin = []
    for key_h, h in enumerate(heightmap):
        for key_e in range(len(h)):
            if check_horizontal(h, key_e) and check_vertical(heightmap, key_h, key_e):
                visited = []
                visited.append((key_h, key_e))
                basin_horizontal_left(heightmap, key_h, key_e, visited)
                basin_horizontal_right(heightmap, key_h, key_e, visited)
                basin_vertical_top(heightmap, key_h, key_e, visited)
                basin_vertical_bottom(heightmap, key_h, key_e, visited)
                basin.append(len(visited))
    print(reduce(lambda x, y: x * y, sorted(basin, reverse=True)[:3]))
def basin_horizontal_right(heightmap, key_h, key_e, visited):
    l = len(heightmap[key_h])-1
    if key_e <= l:
        if heightmap[key_h][key_e] != 9:
            if (key_h, key_e) not in visited:
                visited.append((key_h, key_e))
            if (key_h-1, key_e) not in visited:
                basin_vertical_top(heightmap, key_h-1, key_e, visited)
            if (key_h+1, key_e) not in visited:
                basin_vertical_bottom(heightmap, key_h+1, key_e, visited)
            return basin_horizontal_right(heightmap, key_h, key_e+1, visited)
        else:
            return 0
    else:
        return 0
def basin_horizontal_left(heightmap, key_h, key_e, visited):
    if key_e >= 0:
        if heightmap[key_h][key_e] != 9:
            if (key_h, key_e) not in visited:
                visited.append((key_h, key_e))
            if (key_h-1, key_e) not in visited:
                basin_vertical_top(heightmap, key_h-1, key_e, visited)
            if (key_h+1, key_e) not in visited:
                basin_vertical_bottom(heightmap, key_h+1, key_e, visited)
            return basin_horizontal_left(heightmap, key_h, key_e-1, visited)
        else:
            return 0
    else:
        return 0
def basin_vertical_top(heightmap, key_h, key_e, visited):
    if key_h >= 0:
        if heightmap[key_h][key_e] != 9:
            if (key_h, key_e) not in visited:
                visited.append((key_h, key_e))
            if (key_h, key_e-1) not in visited:
                basin_horizontal_left(heightmap, key_h, key_e-1, visited)
            if (key_h, key_e+1) not in visited:
                basin_horizontal_right(heightmap, key_h, key_e+1, visited)
            return basin_vertical_top(heightmap, key_h-1, key_e, visited)
        else:
            return 0
    else:
        return 0
def basin_vertical_bottom(heightmap, key_h, key_e, visited):
    l = len(heightmap)-1
    if key_h <= l:
        if heightmap[key_h][key_e] != 9:
            if (key_h, key_e) not in visited:
                visited.append((key_h, key_e))
            if (key_h, key_e-1) not in visited:
                basin_horizontal_left(heightmap, key_h, key_e-1, visited)
            if (key_h, key_e+1) not in visited:
                basin_horizontal_right(heightmap, key_h, key_e+1, visited)
            return basin_vertical_bottom(heightmap, key_h+1, key_e, visited)
        else:
            return 0
    else:
        return 0
def check_vertical(heightmap, index_h, index_e):
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
def check_horizontal(line, index):
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
