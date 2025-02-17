
def word_count(file) : 
            words = file.split()
            words = len(words)
            

def charachter_count() : 
    pass

def main() :
        with open("books/frankenstein.txt") as s:
            file_contents = s.read()
            word_count(file_contents)
        

        
main()