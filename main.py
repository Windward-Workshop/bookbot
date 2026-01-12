from stats import *
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


# def get_number_of_words(text):
# split_text = text.split()
# print(f"Found {len(split_text)} total words")
# return len(split_text)


def main():
    # print(
    # f"Found {get_number_of_words(get_book_text('./books/frankenstein.txt'))} total words"
    # )
    # print(get_char_count(get_book_text("./books/frankenstein.txt")))
    # num_words = get_number_of_words(get_book_text("./books/frankenstein.txt"))
    if len(sys.argv) is not 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    num_words = get_number_of_words(get_book_text(sys.argv[1]))

    # chars_dict = get_char_count(get_book_text("./books/frankenstein.txt"))
    chars_dict = get_char_count(get_book_text(sys.argv[1]))

    sorted_chars = get_sorted_chat_count(chars_dict)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        ch = item["char"]
        num = item["num"]
        if ch.isalpha():
            print(f"{ch}: {num}")
    print("============= END ===============")


main()
