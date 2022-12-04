// https://leetcode.com/problems/implement-trie-prefix-tree



class Trie:

    def __init__(self):
        self.trie = dict()
        
    def insert(self, word: str) -> None:
        trie = self.trie
        for char in word:
            if char not in trie:
                trie[char] = dict()
            trie = trie[char]
        trie['*'] = dict()
        
    def search(self, word: str) -> bool:
        trie = self.trie
        for char in word:
            if char not in trie:
                return False
            trie = trie[char]
        return '*' in trie

    def startsWith(self, prefix: str) -> bool:
        trie = self.trie
        for char in prefix:
            if char not in trie:
                return False
            trie = trie[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)