# Solution 1: DFS
from typing import List

class TrieNode:
    def __init__(self):
        self.children = {} # 設置每個 children 為獨立的
        self.isWord = False # 先預設每個 node 都不是單詞的最後一個字，狀態可修改
    
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode() # 如果不存在 就加上去到樹中
            cur = cur.children[c] # 往下一位
        cur.isWord = True # 把最後一個 node 標記狀態為單詞結尾

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for c in words:
            root.addWord(c) # 先把 words 變成 Trie structure
        
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visit or
                board[r][c] not in node.children):
                return # 確保上述情況都不能繼續下一步，超出範圍、有走過、沒有此 node 等
            
            visit.add((r, c)) # 紀錄位置以免重複走到
            node = node.children[board[r][c]] # node 位置移動
            word += board[r][c] # word 位置移動
            if node.isWord:
                res.add(word) # 如果是目標單詞的結尾，加到 res 中

            # 遍歷接下來的每個方位
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "") # 從第一個開始用 for loop 遍歷當字首

        return list(res) # 轉成答案格式