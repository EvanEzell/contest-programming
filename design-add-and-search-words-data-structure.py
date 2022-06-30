// https://leetcode.com/problems/design-add-and-search-words-data-structure

class WordDictionary:

    def __init__(self):
        self.trie = dict()

    def addWord(self, word: str) -> None:
        trie = self.trie
        for char in word:
            if char not in trie:
                trie[char] = dict()
            trie = trie[char]
        trie['*'] = dict()

    def search(self, word: str) -> bool:
        
        def helper(word, trie):
            for i, char in enumerate(word):
                if char == '.':
                    # search all possibilites
                    for key in trie.keys():
                        if helper(word[i+1:], trie[key]):
                            return True
                    return False
                else:
                    if char not in trie:
                        return False
                    trie = trie[char]
            return '*' in trie
        
        return helper(word, self.trie)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)