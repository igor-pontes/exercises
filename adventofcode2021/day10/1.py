chunks = {
    '[': ']',
    '(': ')',
    '{': '}',
    '<': '>'
}
counter = {
    ']': 0,
    ')': 0,
    '}': 0,
    '>': 0
}
points = {
    ']': 57,
    ')': 3,
    '}': 1197,
    '>': 25137
}
def main():
    global counter
    lines = []
    with open('input.txt', 'r') as file:
        while line := file.readline():
            lines.append(line[:-1])
    for line in lines:
        l = [c for c in line]
        visited  = [0 for _ in l]
        find_corrupted(l, 0, 0, visited)
    print(sum(list(map(lambda x: x[1]*points[x[0]], [[x, y] for x, y in zip(counter.keys(), counter.values())]))))

def find_corrupted(line, c_o, c, visited):
    global chunks, counter
    if c+1 > len(visited):
        return (0, "I")
    if visited[c] == 1:
        return find_corrupted(line, c_o, c+1, visited)
    else:
        visited[c] = 1
    if line[c] in list(chunks.values()):
        if line[c] != chunks[line[c_o]]:
            counter[line[c]] += 1
            return (True, line[c])
        return (False, line[c])
    else:
        while temp := find_corrupted(line, c, c+1, visited):
            if temp[0]:
                return temp
            else:
                if temp[1] == chunks[line[c]]:
                    return (False, line[c])
                if temp[0] == "I":
                    return (0, "I")
            if visited.count(0) == 0:
                return (0, "I")
main()
