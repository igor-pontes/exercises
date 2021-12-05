from itertools import repeat
def main():
    vectors = []
    with open('input.txt', 'r') as file:
        while line := file.readline():
            line = line[0:-1]
            temp = [tuple(map(int, [y for y in x.split(",")])) for x in line.split(" -> ")]
            vectors.append(temp)
    vectors = generate(vectors)
    points = {}
    for k1, v1 in enumerate(vectors):
        for k2, v2 in enumerate(vectors):
            if k1 != k2:
                for p in list(v1.intersection(v2)):
                    if p not in points:
                        points.update({p: 1})
                    else:
                        points.update({p: points[p]+1})
    print(len(points))

def generate(vectors):
    cache = []
    for v in vectors:
        temp = []
        if v[0][0] != v[1][0]:
            if v[0][1] != v[1][1]:
                for x in zip(range(v[0][0], v[1][0], 1 if v[0][0] < v[1][0] else -1), range(v[0][1], v[1][1], 1 if v[0][1] < v[1][1] else -1)):
                    temp.append(x)
            else:
                for x in zip(range(v[0][0], v[1][0], 1 if v[0][0] < v[1][0] else -1), repeat(v[1][1])):
                    temp.append(x)
            temp.append(v[1])
            temp.append(v[0])
        elif v[0][0] == v[1][0]:
            for x in zip(repeat(v[0][0]), range(v[0][1], v[1][1], 1 if v[0][1] < v[1][1] else -1)):
                temp.append(x)
            temp.append(v[1])
        cache.append(set(temp))
    return cache
main()
