# week08-5.py 學習計畫 Binary Search第三題
# LeetCode 162. Find Peak Element 找到比左右鄰居大的那個
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #笨方法
        N = len(nums)
        if N==1: return 0

        for i in range(N):
            if i==0:
                if nums[i] > nums[i+1]: return i
            elif i==N-1:
                if nums[i] > nums[i-1]: return i
            elif nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
