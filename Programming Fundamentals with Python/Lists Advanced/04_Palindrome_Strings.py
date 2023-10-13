def palindroe_filtred(word):

    if word == word[::-1]:
        return word


words = input().split()
palindrome_word = input()

palindrome_list = [word for word in words if palindroe_filtred(word)]
palindrome_counter = palindrome_list.count(palindrome_word)

print(palindrome_list)
print(f"Found palindrome {palindrome_counter} times")
