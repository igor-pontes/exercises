from math import floor 
chunks = {
    '[': ']',
    '(': ')',
    '{': '}',
    '<': '>',
}
sequence = []
points = {
    ']': 2,
    ')': 1,
    '}': 3,
    '>': 4
}
scores = []
def main():
    global sequence, scores
    lines = []
    with open('input.txt', 'r') as file:
        while line := file.readline():
            lines.append(line[:-1])
    for line in lines:
        l = [c for c in line]
        visited  = [0 for _ in l]
        temp = []
        while visited.count(0) != 0:
            if complete_line(l, 0, 0, visited, temp) == "Corrupted":
                break
        if temp != []:
            sequence.append(temp)
    for s in sequence:
        total = 0
        for c in s:
            total = total * 5 + points[c]
        scores.append(total)

    print(sorted(scores)[floor(len(scores)/2)])

def complete_line(line, c_o, c, visited, temp):
    global chunks 
    if c+1 > len(visited):
        return "Null"
    if visited[c] == 1:
        return complete_line(line, c_o, c+1, visited, temp)
    else:
        visited[c] = 1
    if line[c] in list(chunks.values()):
        if line[c] != chunks[line[c_o]]:
            return "Corrupted"
        return line[c]
    else:
        while nc := complete_line(line, c, c+1, visited, temp):
            if nc == "Corrupted":
                return nc 
            if nc == chunks[line[c]]:
                return "Match"
            if nc == "Null":
                temp.append(chunks[line[c]])
                return nc 
main()
