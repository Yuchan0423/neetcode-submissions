class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj_list = {i: list() for i in range(numCourses)}

        for pre, course in prerequisites:
            adj_list[course].append(pre)
        
        visited = set()

        checked = [False for _ in range(numCourses)]

        order = list()

        def dfs(node):
            if node in visited:
                return False
            checked[node] = True

            order.append(node)

            visited.add(node)

            for nei in adj_list[node]:
                if not dfs(nei):
                    return False

            visited.remove(node)
            return True

        for i in range(numCourses):
            if checked[i] == False:
                if dfs(i) == False:
                    return []
        
        return order
            
            
