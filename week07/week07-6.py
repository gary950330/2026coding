# week07-6.py 學習計畫 queue 第二題
# LeetCode 649. Dota2 Senate
# Dota2 兩個陣營 the Radiant and the Dire
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque(list(senate))
        banR, banD = 0, 0
        R, D = senate.count('R'), senate.count('D')
        while queue:
            now = queue.popleft()
            if now=='R':
                if banR>0:
                    banR -= 1
                    R -= 1
                    #continue
                else:
                    banD += 1
                    queue.append(now)
            else:
                if banD > 0:
                    banD -= 1
                    D -= 1
                    #continue
                else:
                    banR += 1
                    queue.append(now)

            if R==0: return 'Dire'
            if D==0: return 'Radiant'
