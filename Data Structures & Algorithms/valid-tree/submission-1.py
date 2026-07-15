class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_dic = {i : set() for i in range(n)}
        for i in range(n):
            adj_dic[i].add(i)
        for first, end in edges:
            if adj_dic[first] == adj_dic[end]:
                return False
            
            else:
                union = adj_dic[first] | adj_dic[end]
                for elem in union:
                    adj_dic[elem] = union
        
        return len(adj_dic[0]) == n