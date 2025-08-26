import sys
N = sys.stdin.readline().split()

if int(N[0]) > int(N[1]):
    print(">")
elif int(N[0]) < int(N[1]):
    print("<")
elif int(N[0]) == int(N[1]):
    print("==")
