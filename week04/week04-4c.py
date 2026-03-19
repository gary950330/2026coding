# week04-4c.py (重寫 week04-4b.py)
# LeetCode 3866. First Unique Even Elenent
# 找到陣列 nums 裡 [只出現過1次的偶數] 第一次出現的位置
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        H = Counter(nums)
        for nn in nums:
            if nn % 2 == 0 and H[nn] == 1: return nn
        return -1

# week04-4b.py (重寫 week04-3.py)
        H = [0] * 200
        for nn in nums:
            H[nn] += 1
        for nn in nums:
            if nn %2 == 0 and H[nn] == 1: return nn
        return -1
# week04-3.py More Challenges 的簡單題
        N = len(nums)
        #第一種寫法用陣列
        H = [0] * 200
        for i in range(N):
            H[ nums[i] ] += 1
        for i in range(N):
            if nums[i] % 2 == 0 and H[ nums[i] ] == 1:
                return nums[i] #找到答案了
        return -1
