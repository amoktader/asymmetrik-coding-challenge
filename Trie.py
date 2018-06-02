from Candidate import Candidate

class Trie():
    
    # Constructor
    def __init__(self, candidate):
        self.candidate = candidate
        self.children = {} # Dictionary of candidates
    
    # Adds words to trie
    def addWord(self, str, index=1):
        if index > len(str):
            return
        substr = str[:index].lower()
        if substr not in self.children:
            self.children[substr] = Trie(Candidate(substr, 0))
        if len(str) == index:
            self.children[substr].candidate.updateCount()
            return
        self.children[substr].addWord(str, index+1)
        
    def retrieveWords(self, str, wordList, index=1):
        if len(self.children) == 0:
            return
        str = str.lower()
        if index <= len(str):
            currentPrefix = str[:index]
            if currentPrefix not in self.children:
                return
            childTrie = self.children[currentPrefix]
            candidate = childTrie.candidate
            childTrie.retrieveWords(str, wordList, index+1)
        else:
            for substr in self.children:
                childTrie = self.children[substr]
                candidate = childTrie.candidate
                currentSubstr = candidate.getWord()
                if candidate.isWord():
                    confidence = candidate.getConfidence()
                    wordList.append((currentSubstr, confidence[0], confidence[1]))
                childTrie.retrieveWords(str, wordList, index)
        charToAdd = candidate.getWord()
        if len(str) > 0:
            char = str[0].lower()
            if char not in self.children:
                return
            if charToAdd != '\0':
                currentStr = tempStr + charToAdd
                if candidate.isWord():
                    wordList.append(currentStr, count)
            childTrie.retrieveWords(str[1:], currentStr, wordList)
        else:
            for char in self.children:
                if candidate.isWord():
                    wordList.append(currentStr, count)
                childTrie.retrieveWords(str[1:], currentStr, wordList)
                
