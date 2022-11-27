# for i in range(10):
#     if i > 5 and i % 2 == 0:
#         break
#     print(i)
#     for j in range(101, 105):
#         print(j)
#         if j == 102:
#             break
#     else:
#             print("nested for loop")
#         if not i:
#             print("start for loop")
# else:
#     print("done")

check_migrated = "Filesystem successfully migrated"
lst_migrated = check_migrated.split()
while lst_migrated:
    removed = lst_migrated.pop()
    if removed == "successfully":
        continue
    print("".join(lst_migrated), removed, sep=";")
    if removed.lower() == "filesystem":
        break

else:
    print("next after")

    # while (number := input("enter a number: ")) and not (number.isdigit() and len(number) ==3):
    #     print("error mumber")
    #
    #
    # print(f"end | nuber is {number}")

    # count = int(input("enter your number: "))
    # i = 0
    # while i < count:
    #     i += 1
    #     print(f"iteration N {i}")
    #     if i % 2 != 0:
    #         print(f'{i} < {count}')
    #         continue
    #     print(i)
    #
    # print(f"End")

    for i in range(10):
        if i % 2 == 0:
            print(i)