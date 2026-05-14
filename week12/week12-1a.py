# week12-1a.py 學習計畫 Graph - DFS 第一題 medium題
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = [0]
        visited = set()
        visited.add(0)
        while stack:
            now = stack.pop()
            for k in rooms[now]:
                if k in visited: continue
                # 如果走到這裡,代表沒走過的房間k
                stack.append(k)
                visited.add(k)
        return len(rooms) == len(visited)
