# week08-2.py 學習計畫 Binary Search 第一題
# 給你guess() 你可以呼叫他, 找出1... n 裡面的答案
class Solution:
    def guessNumber(self, n: int) -> int:
        #for i in range(n+1): print( -guess(i), end=' ') #做個實驗
        return bisect_left( range(n+1), 0, key=lambda x:-guess(x) )
        left, right = 1, n+1
        while left < right:
            mid = (left + right) // 2
            if guess(mid)==0: return mid
            if guess(mid)>0: left = mid + 1
            else: right = mid
        return left
