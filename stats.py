def word_counter(text):
        word_list = text.split()
        return len(word_list)

#def letter_counter(text):
        import string
        letters = {letter: 0 for letter in string.ascii_lowercase}
        for letter in text.lower():
                if letter in letters:
                    letters[letter] += 1
        return letters

def letter_counter_2(text):
        letters = {}
        for letter in text.lower():
                if letter.isalpha():
                    letters[letter] = letters.get(letter, 0) + 1
        return letters
                
def character_dictionaries(letters):
       dicts = []
       def sort_on(items):
              return items["num"]
       for letter in letters:
              dicts.append({"char": letter, "num": letters[letter]})
       dicts.sort(reverse=True, key=sort_on) 
       return dicts
