# week07-2.py 學習計畫 Stack 第二題
# LeetCode 735. Asteroid Collision
# 正的向右, 負的向左
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for a in asteroids:
            if a>0:
                ans.append(a)
            else:
                while ans and ans[-1]>0:
                    if abs(ans[-1]) == abs(a):
                        ans.pop()
                        a = 0
                        break
                    elif abs(ans[-1]) > abs(a):
                        a = 0
                        break
                    else:
                        ans.pop() #這裡不用break
                if a != 0: ans.append(a)
        return ans
