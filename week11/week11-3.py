# week11-3.py 學習計畫 Binary Search Tree 第一題 Easy 題
# LeetCode 700. Search in a Binary Search Tree
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def helper(root, val):
            if root==None: return None
            if val < root.val:
                return helper(root.left, val)
            if val > root.val: # 大, 在右邊
                 return helper(root.right, val)
            if val == root.val:
                return root
        return helper(root, val)
