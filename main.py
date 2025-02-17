#main function for the bot
def main() :
            bookpath = "books/frankenstein.txt"
            text = get_book_text(bookpath)
            count = word_count(text)
            charachters = charachter_count(text)
            sorted_dict = sort_dic(charachters)
            report = book_report("Frankenstein", count, sorted_dict)
            print(report)
#the function that gets the text for the book you want to do the report on. 
def get_book_text(path):
    with open(path) as f:
            return f.read()

#funtion that counts the amount of words in the imported book file. 
def word_count(file) : 
            words = file.split()
            return len(words)
            
#function that takes the charachters in the book and get a tally of the total number of times each charachter appears in the book. 
def charachter_count(file) : 
    char_dic = {}
    for char in file: 
        lower_char = char.lower()
        if lower_char in char_dic : 
            char_dic[lower_char] += 1
        else : 
            char_dic[lower_char] = 1
    return char_dic

#function that sorts a dictonary in alphabetical order.
def sort_dic( dic): 

    sorted_dict_by_keys = dict(sorted(dic.items()))
    return sorted_dict_by_keys

#function that prints the report of the book to the console. without the empty spaces, pound symbols and periods
def book_report(book, count, char_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the {book} book")

    filtered_chars = {k: v for k, v in char_count.items() if k not in [" ", "#", "."]}

    for key,values in filtered_chars.items() : 
        print(f"The '{key}'character was found {values} times ")       
    print("-- End report -- ")




        

        
main()