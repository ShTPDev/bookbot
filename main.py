
def word_count(file) : 
            words = file.split()
            return len(words)
            

def charachter_count(file) : 
    char_dic = {}
    for char in file: 
        lower_char = char.lower()
        if lower_char in char_dic : 
            char_dic[lower_char] += 1
        else : 
            char_dic[lower_char] = 1
    return char_dic


def get_book_text(path):
    with open(path) as f:
            return f.read()

def main() :
            bookpath = "books/frankenstein.txt"
            text = get_book_text(bookpath)
            count = word_count(text)
            charachters = charachter_count(text)
            print(charachters)
            print(count)
        

        
main()