class CountSquares:

    def __init__(self):
        self.xy = dict()

    def add(self, point: List[int]) -> None:
        if point[0] not in self.xy:
            self.xy[point[0]] = dict()
        
        if point[1] not in self.xy[point[0]]:
            self.xy[point[0]][point[1]] = 0
        
        self.xy[point[0]][point[1]] += 1

    def count(self, point: List[int]) -> int:
        if point[0] not in self.xy:
            return 0

        ans = 0

        for s in self.xy[point[0]]:
            if s != point[1]:
                point_set = [point[0] + s - point[1], point[0] + point[1] - s]
                for p in point_set:
                    if p in self.xy:
                        ans += self.xy[p].get(point[1], 0) * self.xy[p].get(s, 0) * self.xy[point[0]].get(s, 0)
        
        return ans

        
        
