# week05-5.py 學習計畫 Hash Table (Map/set)
# LeetCode 1657. Determine if two strings are close
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counter1 = Counter(word1)
        counter2 = Counter(word2)

        if set(counter1.keys()) != set(counter2.keys()):
            return False
        # 把出現的次數, 小到大排好,如果兩邊都依樣,那就換到依樣為止
        if sorted(counter1.values()) != sorted(counter2.values()):
            return False
        return True
