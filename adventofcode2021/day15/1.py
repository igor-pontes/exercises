def main():
    directions = {(1, 0), (0, 1)}
    cave = []
    counter = float('inf')
    not_visited = []
    distances = dict()
    with open('input.txt', 'r') as file:
        while line := file.readline():
            cave.append([int(x) for x in line[:-1]])
    
    for y in range(len(cave)):
        for x in range(len(cave[0])):
            distances.update({(x, y): float('inf')})
            not_visited.append((x, y))
    distances[(0,0)] = 0
    target = tuple((len(cave[0])-1, len(cave)-1))
    path(not_visited, cave, directions, distances, target)
    print(distances[(target)])

def path(not_visited, cave, directions, distances, target):
    while len(not_visited) > 0:
        u = min(not_visited, key = lambda x: distances[x])
        dist = distances[u]
        not_visited.remove(u)
        for d in directions:
            v = tuple(map(lambda i, j: i + j, u, d))
            if v[0] > len(cave[0])-1 or v[1] > len(cave)-1:
                continue
            alt = dist + cave[v[1]][v[0]]
            if alt < distances[v]:
                distances[v] = alt

main()
