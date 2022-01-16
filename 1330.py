t = input().split()
t = list(map(int,t))
a,b = t[0],t[1]

if a > b:
    print(">")
elif a == b:
    print("==")
else:
    print("<")
