from AutocompleteProvider import AutocompleteProvider
from Candidate import Candidate
from Trie import Trie
        
if __name__ == '__main__':
    
    autoComplete = AutocompleteProvider()
    
    while True:
        userInput = input('\n\t0: Quit the program.\n' \
                          '\t1: Train autocomplete program.\n' \
                          '\t2: Retrieve next predicted word list.\n' \
                          '\t3: Clear autocomplete program\'s history.\n' \
                          'Select from the options above: ')
        if userInput == "0":
            print("Program ended.")
            break
        elif userInput == "1":
            passage = input("Enter passage to train autocomplete program: ")
            autoComplete.train(passage)
        elif userInput == "2":
            fragment = input("Enter fragment to get autocomplete entries: ")
            wordList = []
            autoComplete.getWords(fragment, wordList)
            for candidate in wordList:
                print(candidate)
        elif userInput == "3":
            del autoComplete
            autoComplete = AutocompleteProvider()
        else:
            print("Invalid input.")
        
