def word_count (text):
    return len(text.split())

def letter_count (text):
    letters ={}
    text = text.lower()
    for char in text:
        if char in letters:
            letters[char] += 1
        else:  
            letters[char] = 1
    return letters

def sort_on(dict):
    return dict["num"]



def main ():
    #This is the report header
    print("--- Begin report of books/frankenstein.txt ---")
   
    # This reads the book to the terminal
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

   # This counts how many words are in the book 
    count = word_count(file_contents)
    print (f"{count} words found in the document\n")

# This tells us how many times a letter occurs
    char_count = letter_count(file_contents)
    char_list = []
    for char in char_count:
        if char.isalpha():
            char_list.append({"char": char, "num": char_count[char]})
    char_list.sort(reverse = True, key = sort_on)
    
    for char_dict in char_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")
    #This prints the report footer.

    print("--- End report ---")


main()
