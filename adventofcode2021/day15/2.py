# A* Part 2
def main():
    directions = {(1, 0), (0, 1), (-1, 0), (0, -1)}
    cave = []
    counter = float('inf')
    openSet = []
    distances = dict()
    scores = dict()
    with open('input.txt', 'r') as file:
        while line := file.readline():
            cave.append([int(x) for x in line[:-1]])
   
    x_len = len(cave[0])
    y_len = len(cave)
    for i in range(4):
        for l in cave:
            line = l[x_len*i:]
            temp = [x for x in line]
            temp = list(map(lambda x: x+1, temp))
            if temp.count(10) > 0:
                temp = list(map(lambda x: x if x <= 9 else 1, temp))
            for x in temp:
                l.append(x)
    for i in range(4):
        base = [x for x in cave[y_len*i:]]
        for l in base:
            temp = [x for x in l]
            temp = list(map(lambda x: x+1, temp))
            if temp.count(10) > 0:
                temp = list(map(lambda x: x if x <= 9 else 1, temp))
            cave.append(temp)
    for y in range(len(cave)):
        for x in range(len(cave[0])):
            distances.update({(x, y): float('inf')})
            scores.update({(x, y): float('inf')})
    target = tuple((len(cave[0])-1, len(cave)-1))        
    distances[(0,0)] = 0
    scores[(0,0)] = heuristic((0,0), target)
    openSet.append((0,0))
    path(openSet, cave, directions, distances, target, scores)
    print(distances[target])

def path(openSet, cave, directions, distances, target, scores):
    while len(openSet) > 0:
        u = min(openSet, key = lambda x: scores[x])
        if u == target:
            return
        dist = distances[u]
        openSet.remove(u)
        for d in directions:
            v = tuple(map(lambda i, j: i + j, u, d))
            if v[0] > len(cave[0])-1 or v[1] > len(cave)-1 or v[0] < 0 or v[1] < 0:
                continue
            alt = dist + cave[v[1]][v[0]]
            if alt < distances[v]:
                distances[v] = alt
                scores[v] = alt + heuristic(v, target)
                if v not in openSet:
                    openSet.append(v)

def heuristic(position, target):
    temp = tuple(map(lambda i, j: i - j, target, position))
    return temp[0] + temp[1]

main()
