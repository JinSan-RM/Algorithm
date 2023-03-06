import sys
sys.stdin = open('input.txt')

for _ in range(1, 11):
    tc = int(input())
    sadari = list(list(map(int, input().split())) for _ in range(100))

    s = sadari[99].index(2)
    row = 99
    col = s
    visited = [[0] * 100 for _ in range(100)]
    while row != 0:
        visited[row][col] = 1
        if col - 1 >= 0 and sadari[row][col - 1] and visited[row][col - 1] == 0:
            col -= 1
            continue
        elif col + 1 < 100 and sadari[row][col + 1] and visited[row][col + 1] == 0:
            col += 1
            continue
        else:
            row -= 1

    answer = col

    print(f'#{tc} {answer}')