# week05-6.py 學習計畫 Hash Table (Map/set) 第四題
# LeetCode 2352. Equal Row and Column Pairs
# 橫的直的,相同的有幾組
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        counter = Counter()
        for row in grid:
            counter[ tuple(row) ] += 1

        ans = 0 # 有幾組?
        for col in zip(*grid):
            ans += counter[ tuple(col) ]
        return ans
