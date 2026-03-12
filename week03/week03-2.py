# week03-2.py 學習計畫 Sliding Window 第一題
# LeetCode 643. Maximum Average Subarray I
# 用 Sliding Window 毛毛蟲的寫法
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        N = len(nums)
        total = sum( nums[:k] )
        maxTotal = total
        for i in range(k, N):
            total = total + nums[i] - nums[i-k]
            # nums[i]右邊的頭(往右吃), nums[i-k]左邊的尾,吐出來
            maxTotal = max(maxTotal, total)
        return maxTotal / k # 最大的平均 = 最大的Total / k
