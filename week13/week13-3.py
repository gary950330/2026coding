# week13-3.py 學習計畫 Heap / Priority 第一題
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #先用作弊的寫法示範一次
        #nums.sort(reverse=True)
        #return nums[k-1]

        #要用 Heap 資料結構, 可以找出最小的數
        #heapify(nums) # 變成 heap 資料結構
        #while nums:
        #   print( heappop(nums) )

        #最後用這個版本
        heapify(nums)
        for i in range(len(nums)-k):
            heappop(nums)
        return heappop(nums)
