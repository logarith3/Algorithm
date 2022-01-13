t = input()
t = int(t)

if t % 4 == 0:
    if t % 400 == 0 or t % 100 != 0:
        print(1)
else:
    print(0)
