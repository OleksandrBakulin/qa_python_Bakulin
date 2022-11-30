text = input("enter you text here: ")
clear_text = ""
for digit in text:
    if digit not in ('0','1','2','3','4','5','6','7','8','9'):
        clear_text = clear_text + digit
print(clear_text)