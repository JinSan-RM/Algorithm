import sys
N = sys.stdin.readline().split()

hour = int(N[0])
minute = int(N[1])

if minute < 60:
    res_min = minute - 45
    if res_min < 0:
        res_min = 60 + res_min
        hour += -1


if hour < 0:
   hour = hour + 24

print(hour, res_min)


