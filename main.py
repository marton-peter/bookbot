import sys
from stats import get_word_count, get_character_count

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    character_count = get_character_count(book_text)
    character_list = list(character_count.items())
    character_list.sort(reverse=True, key=sort_on)

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in character_list:
        print(f"{i[0]}: {i[1]}")
    print("============= END ===============")

def get_book_text(path): # Opens file and extracts text as string.
    with open(path) as f:
        return f.read()
    
def sort_on(item): # Retrieves a key for sorting.
    return item[1]
        
main()