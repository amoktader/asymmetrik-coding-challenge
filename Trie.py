from Candidate import Candidate

class Trie():
    
    # Constructor
    def __init__(self, candidate):
        self.candidate = candidate
        self.children = {} # Dictionary of candidates
    
    # Add words to trie
    def addWord(self, str, index=1):
        if index > len(str):
            return
        substr = str[:index].lower() #store letter-by-letter, e.g. "the" --> "t", "th", "the"
        if substr not in self.children:
            self.children[substr] = Trie(Candidate(substr, 0))
        if len(str) == index: #if word ends, update word count and return
            self.children[substr].candidate.updateCount()
            return
        self.children[substr].addWord(str, index+1)
    
    # Look through Trie for words
    def retrieveWords(self, str, wordList, index=1):
        if len(self.children) == 0:
            return
        str = str.lower()
        if index <= len(str): #if still looking for the fragment
            currentPrefix = str[:index]
            if currentPrefix not in self.children: #if fragment not found in Trie, return
                return
            childTrie = self.children[currentPrefix]
            candidate = childTrie.candidate
            if index == len(str) and candidate.isWord(): #edge case if fragment is a word
                currentSubstr = candidate.getWord()
                confidence = candidate.getConfidence()
                wordList.append((currentSubstr, confidence[0], confidence[1]))
            childTrie.retrieveWords(str, wordList, index+1)
        else: # start looking for all words with the prefix
            for substr in self.children:
                childTrie = self.children[substr]
                candidate = childTrie.candidate
                currentSubstr = candidate.getWord()
                if candidate.isWord():
                    confidence = candidate.getConfidence() # store confidence for sorting
                    wordList.append((currentSubstr, confidence[0], confidence[1]))
                childTrie.retrieveWords(str, wordList, index)
