post = input("eneter your mail: ")

if (post.find("@") != -1 ) and (post.find(".") != -1):
    print("Yes")
else:
    print("no")