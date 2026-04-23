# week08-4.py 學習計畫 Binary Search 第二題
# LeetCode 2300. Successful pairs of spells and potions
# 想知某種 spells[i] 魔法, 配幾種藥水可以成功
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        P = len(potions)
        ans = []
        for spell in spells:
            now = P - bisect_left(potions, success/spell)
            ans.append(now)
        return ans
