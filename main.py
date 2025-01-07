def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    character_count = get_character_count(book_text)
    character_list = list(character_count.items())
    character_list.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document.")
    for i in character_list:
        print(f"The '{i[0]}' character was found {i[1]} times.")
    print("--- End report ---")

def get_book_text(path): # Opens file and extracts text as string.
    with open(path) as f:
        return f.read()
    
def get_word_count(text): # Counts words after splitting the string.
    return (len(text.split()))

def get_character_count(text): # Counts characters after converting the string to lower case.
    count = {}
    for c in text.lower():
        if c.isalpha(): # Only counts alphabetic characters.
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
    return count

def sort_on(item): # Retrieves a key for sorting.
    return item[1]
        
main()