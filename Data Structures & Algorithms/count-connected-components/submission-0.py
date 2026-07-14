class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        components = dict()

        for i in range(n):
            components[i] = i
        
        component_sets = dict()

        for i in range(n):
            node = set()
            node.add(i)
            component_sets[i] = node
        
        for start, end in edges:
            if components[start] != components[end]:
                endpoint = components[end]
                for connect in component_sets[components[end]]:
                    components[connect] = components[start]
                component_sets[components[start]] = component_sets[components[start]] | component_sets[endpoint]
                component_sets.pop(endpoint)
        
        return len(component_sets)