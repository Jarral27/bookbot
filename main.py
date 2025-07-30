import sys
from stats import word_count
from stats import get_chars_dict
from stats import sort_chars_dict

def get_book_text(path):
    with open(path) as book_file:
        book_text = book_file.read()
    return book_text

def print_report(book_path, num_words, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for key in sorted_chars:
        if not key["char"].isalpha():
            continue
        print(f"{key['char']}: {key['num']}")

    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = word_count(text)
    chars_dict = get_chars_dict(text)
    sorted_chars = sort_chars_dict(chars_dict)
    
    print_report(book_path, num_words, sorted_chars)

main()
