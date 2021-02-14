'''
Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split its set of nodes into two independent subsets A and B, such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists. Each node is an integer between 0 and graph.length - 1.

There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.
'''

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        Set = {}
        def dfs(n):
            for i in graph[n]:
                if i in Set:
                    if Set[i] == Set[n]:
                        return False
                else:
                    Set[i] = 1 - Set[n]
                    if not dfs(i):
                        return False
            return True
        for i in range(len(graph)):
            if i not in Set:
                Set[i] = 0
                if not dfs(i):
                    return False
        return True
