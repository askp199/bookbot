#This is the main python file for my bookbot

def main():

    #sets path to file and reads it in
    book = 'Frankenstein'
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read()

    #Counts the words in a book
    def word_count():
        words = file_contents.split()
        count = len(words)
        return count

    # Counts the letters in the book
    def letter_count():
        lower_case_file = file_contents.lower()
        letter_count_dict = {}

        for i in lower_case_file:
            if i in letter_count_dict:
                temp = letter_count_dict[i]
                temp += 1
                letter_count_dict[i] = temp
            else: 
                letter_count_dict[i] = 1
        
        return letter_count_dict
    
    #Generates a report including the word count and the letter count of the book
    def report():
        word = word_count()
        letter = letter_count()
        list_dict = []
        
        #sorts the letters in alphabetical order
        my_keys = list(letter.keys())
        my_keys.sort()
        sorted_dict = {i: letter[i] for i in my_keys}
        print(sorted_dict)

        #creates a new list with only alphabet characters
        for i, val in sorted_dict.items():
            key = f"{i}"
            if i.isalpha():
                new_dict = {}
                new_dict[key]=val
                list_dict.append(new_dict)

        #Prints the text of the report
        print(f"------Begin report on {book}-----")
        print("")
        print(f"The word count is {word}.")
        print(f"")

        for i in range(len(list_dict)):

            dictonary = list_dict[i]
            for keys, value in dictonary.items():
                new_string = f"The letter {keys} was found {value} times."
                print(new_string)

        print("")
        print(f"-----End Report-----")

    
    report()


if __name__ == '__main__':
    main()


