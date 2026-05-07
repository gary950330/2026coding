# week11-1a.py 學習計畫 Binary Tree - DFS 第二題 Easy題
# LeetCode 872. Leaf-Simlar Trees
# 想知道 binary tree 裡的 leaf 組出來 是否都相同
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        a = []
        def helper(root):
            if root.left == None and root.right == None:
                a.append( root.val )
            if root.left: helper(root.left)
            if root.right: helper(root.right)
        helper(root1)
        a, b = [], a
        helper(root2)
        print('a', a)
        print('b', b)
        return a == b
