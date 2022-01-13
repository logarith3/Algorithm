t = input().split()
t = list(map(int,t))

if t[0] == 0:
    h = 24
    m = t[1]
else:
    h = t[0]
    m = t[1]

r = h*60+m-45

print(r // 60,r % 60)
