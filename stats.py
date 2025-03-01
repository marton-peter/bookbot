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
