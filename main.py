from stats import get_num_words, get_num_char, get_num_char_sorted
import sys
ARGS = sys.argv
if len(ARGS) != 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

def get_book_text(filepath: str) -> str:
    with open(filepath) as book:
        return book.read()
def main():
    file_location = ARGS[1]
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {file_location}...')
    print('----------- Word Count ----------')
    get_num_words(get_book_text(file_location))

    char_dict_list = get_num_char_sorted(get_num_char(get_book_text(file_location)))

    print('--------- Character Count -------')
    for pair in char_dict_list:
        if pair["char"].isalpha():
            print(f"{pair["char"]}: {pair["num"]}")
    
    print('============= END ===============')

main()