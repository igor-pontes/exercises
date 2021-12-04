def main():
    numbers = None
    boards = [] 
    
    with open('input.txt', 'r') as file:
        numbers = file.readline()[0:-1].split(",")
        temp = []
        while line := file.readline():
            if line != '\n':
                temp.append(line[0:-1])
            else:
                if temp != []:
                    boards.append(temp)
                    temp = []
        boards.append(temp)

    result = run(numbers, boards)

    print(f'{result}')

def run(numbers, boards):
   boards_cache = [[] for _ in range(len(boards))]
   for number in numbers:
        for (board_key, board) in enumerate(boards):
            if check(number, board, board_key, boards_cache):
                return board_sum(board, boards_cache[board_key])*int(boards_cache[board_key][-1])

def check(number, board, board_key, boards_cache):
    for b in board:
        for c in b.split():
            if int(c) == int(number):            
                boards_cache[board_key].append(number)
                if checkrows(board, boards_cache[board_key]) or checkcolumns(board, boards_cache[board_key]):
                    return True


def checkrows(board, board_cache):
    for b in board:
       if set(b.split()).issubset(set(board_cache)):
            return True

def checkcolumns(board, board_cache):
    columns = [[] for _ in range(len(board[0].split()))]
    for c in range(len(board[0].split())):
        for b in board:
            columns[c].append(b.split()[c])
    for c in columns:
       if set(c).issubset(set(board_cache)):
            return True

def board_sum(board, boards_cache):
    temp = [int(x) for x in boards_cache]
    unmarked = 0
    for b in board:
        for n in b.split():
            if int(n) not in temp:
                unmarked = unmarked + int(n)
    
    return unmarked

main()
