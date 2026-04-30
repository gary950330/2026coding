# week10-2a.py 學習計畫 Binary Search Tree - DFS
# DFS 深度優先搜尋 tree最喜歡用函式搜尋函式來解
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if root == None: return 0 #沒有東西
            left = helper(root.left)
            right = helper(root.right)
            return max(left, right) + 1
        return helper(root)
