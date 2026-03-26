# week05-4.py 昨天 2026-03-25的挑戰題
# LeetCode 3456. Equal Sum Grid Partition I
# grid 矩陣 能否切一刀 兩邊和 剛好相同
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = sum( [sum(row) for row in grid] ) #全部加起來

        preSum = 0 #橫切
        for row in grid:
            preSum += sum(row)
            if preSum == total - preSum:
                return True

        preSum = 0 #直切
        for col in zip(*grid):
            preSum += sum(col)
            if preSum == total - preSum:
                return True

        return False
