# week03-3.py 學習計畫 Sliding Window 第二題
# LeetCode 1456. Maximum Number of Vowels in a Substring of Given Length
# 母音 Vowels: a,e,i,o,u 長度k的小字串,最多幾個母音
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou') #把5個字母,變成set()
        # 以後用 if c in vowels: 就可以快速確認它是母音
        # 以前 if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
        count = 0 # 紀錄目前有幾個母音
        for i in range(k):
            if s[i] in vowels: count += 1
        ans = count # 離開迴圈時
        N = len(s)
        for i in range(k, N):
            if s[i] in vowels: count += 1
            if s[i-k] in vowels: count -= 1
            ans = max(ans, count) #更新答案, 找最大值
        return ans
