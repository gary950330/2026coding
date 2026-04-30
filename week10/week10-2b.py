# week10-2b.py 學習計畫 Binary Search Tree - DFS
# DFS 深度優先搜尋 tree最喜歡用函式搜尋函式來解
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
            if root == None: return 0 #沒有東西
            return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1
