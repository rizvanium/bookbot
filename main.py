def main():
    path_to_book = "./books/frankenstein.txt"
    print(f"--- Begin report of {path_to_book} ---")
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()

        word_count = get_word_count(file_contents)
        print(f"{word_count} words found in the document\n")

        char_map = get_char_map(file_contents)
        display_char_map(char_map)
    print(f"--- End report ---")

def get_word_count(str):
    return len(str.split())

def get_char_map(str):
    char_count = {}
    for letter in str.lower():
        if letter in char_count:
            char_count[letter] += 1
        else:
            char_count[letter] = 1
    return char_count

def display_char_map(char_map):
    for ch in dict(sorted(char_map.items(), key=lambda item: item[1], reverse=True)):
        if ch.isalpha():
            print(f"The '{ch}' character was found {char_map[ch]} times")


main()