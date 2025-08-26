import sys
while True:
    N = sys.stdin.readline().split()

    if N[0] == "0" and N[1] == "0":
        break

    else:
        print( int(N[0]) + int(N[1]) )
