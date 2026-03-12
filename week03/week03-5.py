# week03-5.py 學習計畫 Sliding Window 第四題
# LeetCode 1493. Longest Subarray of 1s After Deleting One Element
# 陣列裡, 一定要刪掉一個, 問剩下的陣列裡,最長的1有幾個?
# Sliding Window 伸縮自如的蛇蛇, 肚子裡, 可容忍最多1個0
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        N = len(nums) #陣列長度
        zeros = 0
        tail = 0
        ans = 0
        for head in range(N):
            if nums[head]==0: zeros += 1
            while zeros > 1:
                if nums[tail]==0: zeros -= 1
                tail += 1
            ans = max(ans, head - tail + 1)
        return ans - 1
