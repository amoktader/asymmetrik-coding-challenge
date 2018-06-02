from Candidate import Candidate
from Trie import Trie

class AutocompleteProvider():
    
    # Constructor
    def __init__(self):
        self.trie = Trie(Candidate("", 0))
        # Blacklist to handle words with punctuation in them. Would use regex in a real time scenario.
        self.wordsWithPunctuation = { "a.m.", "p.m.", "jr.", "sr.", "dr.", "etc.", "mr.", "ms." }
        
    # Get words to be autocompleted with the fragment
    def getWords(self, fragment, wordList):
        self.trie.retrieveWords(fragment, wordList, 1)
        wordList.sort(key=lambda x: (x[1], x[2]), reverse=True)
        for i in range(len(wordList)):
            wordList[i] = (wordList[i][0], wordList[i][1])
    
    # Stores the words in the program
    def train(self, passage):
        print("hello")
        for word in passage.split():
            retWord = self.__stripPunctuation(word)
            self.trie.addWord(retWord)
    
    # Strips punctuation from the word
    def __stripPunctuation(self, word):
        retWord = word
        start = 0
        # Strips punctuation from beginning
        while start < len(word) and not word[start].isalpha():
            retWord = word[start+1:]
            start += 1
        word = retWord
        end = len(word) - 1
        # Strips punctuation from end
        while end >= 0 and retWord not in self.wordsWithPunctuation and not word[end].isalpha():
            retWord = word[:end]
            end -= 1
        return retWord