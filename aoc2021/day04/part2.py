import numpy as np


def read_input_objs():
    # for puzzles with newline-separated objects as input
    with open('input.txt') as fh:
        boards = []
        obj = []
        i = 0
        for line in fh.readlines():
            i += 1
            if i == 1:
                nums = line.strip().split(',')
                continue
            if i == 2:
                continue
            if not line.strip():
                boards.append(obj)
                obj = []
            else:
                obj.append(line.strip().split())
        if obj:
            boards.append(obj)
        return nums, boards


def is_winner(board):
    b = np.array(board)
    for r in range(b.shape[0]):
        if ''.join(b[r, :]) == 'XXXXX':
            return True
    for c in range(b.shape[1]):
        if ''.join(b[:, c]) == 'XXXXX':
            return True
    return False


def paint(num, board):
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == num:
                board[r][c] = 'X'


def sum_non_x(board):
    s = 0
    for r in range(len(board)):
        for c in range(len(board[0])):
            p = board[r][c]
            if p != 'X':
                s += int(p)
    return s


def main():
    nums, boards = read_input_objs()
    print(nums)
    for b in boards:
        for l in b:
            print(l)
        print('')

    win_boards = set()
    for n in nums:
        for bi in range(len(boards)):
            b = boards[bi]
            paint(n, b)
            if is_winner(b) and bi not in win_boards:
                win_boards.add(bi)
                if len(win_boards) == len(boards):
                    s = sum_non_x(b)
                    print(s, n)
                    return s * int(n)


res = main()
print(res)