# week09-2.py 學習計畫 Linked List 第三題 easy題
# LeetCode 206. Reverse Linked List
# 把它反過來
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = [] #容易理解的方法
        while head:
            a.append( head.val )
            head = head.next
        #print(a)
        now = ans = ListNode()

        # 下面用倒過來的迴圈,成功變成我們習慣的陣列
        N = len(a)
        for i in range(N-1, -1, -1):
            now.next = ListNode(a[i])
            now = now.next
        return ans.next
