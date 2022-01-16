t1 = list(map(int,input().split()))
t2 = list(map(int,input().split()))
r = []

for i in range(0,t1[0]):
    if t2[i] < t1[1]:
        r.append(t2[i])

for i in r:
    print(i, end=' ')
