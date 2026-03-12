# week03-4.py 學習計畫 Sliding Window 第三題
# LeetCode 1004. Max Consecutive Ones III
# 你可以把 K 個0都轉變成1 那最長的一堆1,有幾個1
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = 0
        N = len(nums)
        ans = 0
        tail = 0
        for head in range(N):
            if nums[head]==0:
                zeros += 1
                #if zeros > k:
                while zeros > k:
                    if nums[tail]==0:
                        zeros -= 1
                    tail += 1 # 尾巴
            # 排毒完畢, 身體內保證不會有太多的[有毒的0]
            ans = max(ans, head - tail + 1)
        return ans
