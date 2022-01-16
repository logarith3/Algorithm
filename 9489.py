t = input()
t = int(t)

if t >= 90:
    print("A")
elif t >= 80:
    if t <= 89:
        print("B")
elif t >= 70:
    if t <= 79:
        print("C")
elif t >= 60:
    if t <= 69:
        print("D")
else:
    print("F")
