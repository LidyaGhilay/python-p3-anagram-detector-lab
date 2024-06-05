# your code goes here!# lib/anagram.py

class Anagram:
    def __init__(self, word):
        self.word = word.lower()  
    
    def match(self, word_list):
        anagrams = []
        for words in word_list:
            
            if words.lower() != self.word and sorted(words.lower()) == sorted(self.word):
                anagrams.append(words)
        return anagrams
