'''
212. Word Search II
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.ended = False
        
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.ended = True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        ROWS, COLS = len(board), len(board[0])
        
        res, visited = set(), set()
        
        def dfs(r,c,node,word):
            if (r < 0 or c < 0 
                or r == ROWS or c == COLS 
                or (r,c) in visited 
                or board[r][c] not in node.children):
                    return
            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.ended == True:
                res.add(word)
            
            dfs(r - 1,c,node,word)
            dfs(r + 1,c,node,word)
            dfs(r,c - 1,node,word)
            dfs(r,c + 1,node,word)
            
            visited.remove((r,c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root,"")
        return list(res)
'''
Runtime: 7846 ms, faster than 34.75% of Python3 online submissions for Word Search II.
Memory Usage: 14.6 MB, less than 65.12% of Python3 online submissions for Word Search II.
'''