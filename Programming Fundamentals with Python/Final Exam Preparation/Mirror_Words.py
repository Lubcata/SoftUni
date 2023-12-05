import re


def main():
    text = input()
    pattern = r"([@#])([a-zA-Z]{3,})(\1)(\1)([a-zA-Z]{3,})(\1)"
    match = re.findall(pattern, text)
    mirror_words = []
    count_of_words = len(match)

    for word in match:
        if word[1] == word[4][::-1]:
            mirror_words.append(f"{word[1]} <=> {word[4]}")

    if count_of_words > 0:
        print(f"{count_of_words} word pairs found!")
        if mirror_words:
            print("The mirror words are:")
            print(', '.join(mirror_words))
        else:
            print("No mirror words!")
    else:
        print("No word pairs found!")
        print("No mirror words!")


main()
