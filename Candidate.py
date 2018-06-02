from datetime import datetime

class Candidate():
    
    # Constructor
    def __init__(self, substr, count):
        self.substr = substr
        self.count = count
        self.timestamp = datetime.now()
        
    # Gets the current substring
    def getWord(self):
        return self.substr
    
    # Gets the count of the word as well as the most recent usage
    def getConfidence(self):
        return (self.count, self.timestamp)
    
    # If current node produces a word
    def isWord(self):
        return self.count > 0
    
    # Add 1 to count of word + new timestamp
    def updateCount(self):
        self.count += 1
        self.timestamp = datetime.now()