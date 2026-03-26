# week05-3.py 學習計畫 Hash Table (Map/Set)
# LeetCode 1287. Unique Number of Occurrences
# 每種數字, 出現的次數必須都不一樣喔
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        s = set()
        for c in counter:
            #測試一下
            #print(c, counter[c])
            # 問 counter[c] 是否獨一無二
            if counter[c] in s:
                return False
            s.add( counter[c] )
        return True #隨便return值
