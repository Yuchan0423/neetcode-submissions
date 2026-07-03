class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if numCourses == 0 or prerequisites == []:
            return True

        adjacency_graph = {}

        for a, b in prerequisites:
            if a not in adjacency_graph:
                adjacency_graph[a] = set()
            if b not in adjacency_graph:
                adjacency_graph[b] = set()
            adjacency_graph[a].add(b)
        
        all_courses = set(adjacency_graph.keys())
        
        start = prerequisites[0][0]
        
        connected = set()
        connected.add(start)

        points = deque()
        points.append(start)

        while points:
            for _ in range(len(points)):
                check = points
                point = points.popleft()
                for neighbor in adjacency_graph[point]:
                    if neighbor in connected and neighbor not in check:
                        return False
                    connected.add(neighbor)
                    points.append(neighbor)
        
        remaining_points = all_courses - connected
        remaining_graph = {}
        for remaining_point in remaining_points:
            remaining_graph[remaining_point] = adjacency_graph[remaining_point] - connected
        
        remaining_prerequisite = []

        for remaining_point in remaining_points:
            for end in remaining_graph[remaining_point]:
                remaining_prerequisite.append([remaining_point, end])

        return self.canFinish(len(remaining_points), remaining_prerequisite)


