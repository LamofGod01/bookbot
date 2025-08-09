def get_book_text(filepath):
        with open(filepath) as f:
                return f.read()
        
from stats import word_counter
from stats import letter_counter_2
from stats import character_dictionaries

def main():
        import sys
        try:
            book_location = sys.argv[1]
        except Exception as e:
               print("Usage: python3 main.py <path_to_book>")
               sys.exit(1)
        book_text = get_book_text(book_location)
        word_count = word_counter(book_text)
        letter_counts = character_dictionaries(letter_counter_2(book_text))
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_location}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for i in range(0,len(letter_counts)):
                print(f"{letter_counts[i]["char"]}: {letter_counts[i]["num"]}")
        print("============= END ===============") 






main()