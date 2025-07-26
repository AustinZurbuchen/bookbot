from stats import count_words, count_letters
import sys

def get_book_text(file_path):
    with open(file_path, encoding='utf-8') as f:
        file_contents = f.read()
        return file_contents

def main():
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(args[1])
    characters = count_letters(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book fount at {args[1]}")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_text)} total words")
    print("----------- character Count -----")
    for letter in sorted(characters, key=characters.get, reverse=True):
        if letter.isalpha():
            print(f"'{letter}': {characters[letter]}")
    print("============ END ================")

main()