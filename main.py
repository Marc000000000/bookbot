from stats import get_wordcount, get_charcount, chars_dict_to_sorted_list
import sys


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def main():
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    wordcount = get_wordcount(text)
    charcount = get_charcount(text)
    sorted_charcount = chars_dict_to_sorted_list(charcount)
    print ((f"Found {wordcount} total words"))
    print(charcount)
    print(sys.argv)

    print_report(filepath, wordcount, sorted_charcount)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def print_report(filepath, wordcount, sorted_charcount):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {wordcount} total words")
    print("--------- Character Count -------")
    for item in sorted_charcount:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()
    
