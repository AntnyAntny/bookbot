def main():
    wordcount = 0
    letter_dict = {}
    full_dict = []
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        lowercaseLetters = file_contents.lower()
        words = lowercaseLetters.split()
    
        for w in words:
            #word counter
            wordcount +=1
            #letter organizer using a dictionary
            letters = [*w]
            for l in letters:
                if l in letter_dict:
                     letter_dict[l] +=1
                else:
                    letter_dict[l] = 1
        
        #revising the dictionary into a list of dictionaries with a letter and count key
        for letter in letter_dict:
            count = letter_dict[letter]
            character_dict = {
                "letter": letter,
                "count": count
            }
            full_dict.append(character_dict)
        
        
        #sorting function to sort list outputs by count value(highest first)
        def sort_value(dict):
            return dict["count"]
        
        def sort_alpha(dict):
            return dict["letter"]
        

        #Prints the report, including the word count and the character count list
        def report():
            print("""
----------------Book Report----------------


       -----Word Count-----
""")
            print(f"The word count for this book is {wordcount}.")
            print("""

    -----Character Count-----
""")
            for letter in full_dict:
                if letter["letter"].isalpha():
                    print(f"The character '{letter["letter"]}' appears {letter["count"]} times.")
        
#Report
    #Introdction to Main report
    print("""
        -----Welcome to the book report!-----
Before we begin, would you like the word count organized either;
Alphabetically? Or in descending order(starting with the letter that appeared the most in the book)?
""")
    
    answer = input("Press 1 for alphabetically or 2 for descending order! ")
    if answer == "1":
        full_dict.sort(reverse=False, key=sort_alpha)
        print("""
You have chosen your character count to be listed alphabetically!
Here is your book report!
""")
        report()

    elif answer == "2":
        full_dict.sort(reverse=True, key=sort_value)
        print("""
You have chosen your character count to be listed in descending order!
Here is your book report!
""")
        report()
    else:
        print("That is not a proper response. Please try again! :(")



main()