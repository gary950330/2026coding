# week11-1b.py 學習計畫 Binary Tree - DFS 第二題 Easy題
# LeetCode 872. Leaf-Simlar Trees
# 想知道 binary tree 裡的 leaf 組出來 是否都相同
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        a, b = [], []
        def helper(root, a):
            if root.left == None and root.right == None:
                a.append( root.val )
            if root.left: helper(root.left, a)
            if root.right: helper(root.right, a)
        helper(root1, a)
        helper(root2, b)
        return a == b
