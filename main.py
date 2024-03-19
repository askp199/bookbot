#This is the main python file for my bookbot

def main():

    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read()

    def word_count():
        words = file_contents.split()
        count = len(words)
        return count


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
    
    def report():
        word = word_count()
        letter = letter_count()
        list_dict = []
        for i, val in letter.items():
            key = f"{i}"
            if i.isalpha():
                new_dict = {}
                new_dict[key]=val
                list_dict.append(new_dict)
        
        print(list_dict)
    
    report()




if __name__ == '__main__':
    main()


