// https://leetcode.com/problems/word-search-ii

class Trie:
    def __init__(self, words = None):
        self.children = dict()
        self.word = None
        self.count = 1
        
        if words:
            for w in words:
                self._insert(w)
        
    def _insert(self, word):
        trie = self
        for char in word:
            if char in trie.children:
                trie[char].count += 1
            else:
                trie.children[char] = Trie()   
            trie = trie[char]
        trie.word = word
    
    def _found(self, word):
        trie = self
        for char in word:
            trie[char].count -= 1
            trie = trie[char]
        
    def __contains__(self, char):
        if char in self.children:
            return True
        else:
            return False
        
    def __getitem__(self, char):
        if char in self.children:
            return self.children[char]
        else:
            raise KeyError()     
        
    def __repr__(self):
        result = ""
        if self.word:
            result += "*" + self.word + " "
        result += str(self.count)
        if self.children:
            result += ' ' + str(self.children)
        return result

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        self.trie = Trie(words)
        self.found = set()
        
        def neighbors(i, j):
            dirs = [(1,0), (0,1), (-1,0), (0,-1)]
            
            result = []
            for x, y in dirs:
                if 0 <= i+x < len(board) and 0 <= j+y < len(board[0]):
                    result.append((i+x,j+y))
            return result
        
        def dfs(i, j, trie = self.trie, visited = set()):
            
            char = board[i][j]
            
            if (i, j) in visited or char not in trie:
                return
            
            trie = trie[char]
            
            if trie.count == 0:
                return
            
            visited.add((i, j))
            
            if trie.word and trie.word not in self.found:
                self.found.add(trie.word)
                self.trie._found(trie.word)
            
            for x, y in neighbors(i, j):
                dfs(x, y, trie, visited)
            
            visited.remove((i,j))
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j)
                    
        return self.found