N = int(input("enter the width of triangle: "))
for i in range(N + 1):
    if i <= N:
        print(((N - i) * " ") + (i * "*"))
        i -= 1

