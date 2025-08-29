import sys
S = sys.stdin.readline()
S = [i.upper() for i in S]

S.pop()
res = {}
for i in S:
    res[i] = res.get(i, 0 ) + 1
result = [k for k, v in res.items() if max(res.values()) == v]
if len(result) > 1:
    print("?")
else:
    print(result[0])
