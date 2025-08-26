import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    position = [[0, 1], [1, 0]]
    board = [list(map(int, input().split())) for _ in range(N)]
    for row in range(len(board)):
        minimum = 0
        minimum_col = 0
        minimum_row = 0
        for col in range(len(board)):
            if board[position[0]] >= board[position[1]]:
                print(board[position[0]])

