N = int(input("enter the width of triangle: "))
for i in range(N):
    if i != N:
        print(((i * " ") + (N - i) * "*"))
        i += 1
