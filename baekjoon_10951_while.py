import sys
while True:
    try:
        A, B = map(int, sys.stdin.readline().strip().split()) 

    except EOFError:
        break
        
    except ValueError:
        break
        
    print(A+B)
