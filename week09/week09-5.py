# week09-5.py 學習計畫 Linked List 第一題 Medium 有點難 把中間的node刪掉
# LeetCode 2095. Delete the Middle Node of a Linked List
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None: return None

        prev = fast = slow = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            prev = slow # 烏龜在走前, 先記下前一格的位置
            slow = slow.next
        #print( slow.val )
        prev.next = slow.next
        return head
