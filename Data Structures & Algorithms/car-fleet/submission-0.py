class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dic = dict()
        for pos, vol in zip(position, speed):
            dic[pos] = vol
        
        position.sort()

        group = 1
        track = position[-1]

        while position:
            pos = position.pop()
            if (target - pos) * dic[track] > (target - track) * dic[pos]:
                track = pos
                group += 1

        
        return group
            