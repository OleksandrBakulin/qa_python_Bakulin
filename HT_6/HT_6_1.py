# 1)
the_word = input("type the word to check if it  palindrome: ")
palindrome = the_word[::-1]
if palindrome == the_word:
    print(f"+, the backwards of {the_word} are {palindrome} ")
else:
    print(f"-, {the_word} can't be reversed as palindrome")



