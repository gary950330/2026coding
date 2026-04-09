# week07-5.py學習計畫 Queue 第1題
# 933. Number of Recent Calls 想知道3000 範圍內,有幾個ping
class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t) #從右邊塞入
        while self.queue[0] < t-3000: #目前最左邊,最古老的t)
             self.queue.popleft()
        return len(self.queue)



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
