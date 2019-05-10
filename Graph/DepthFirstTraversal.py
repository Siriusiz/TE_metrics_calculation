# Program to perform depth first traversal in a graph
from collections import defaultdict

class Graph:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.edge_weight = defaultdict(list)
        self.directed = directed
        self.vertices = []

    def addEdge(self, frm, to, weight):          # if weight == 0 : information
        if frm not in self.vertices:             # elif weight == 1 : material
            self.vertices.append(frm)
        if to not in self.vertices:
            self.vertices.append(to)

        self.graph[frm].append(to)
        self.edge_weight[frm].append((to, weight))

        if self.directed is False:
            self.graph[to].append(frm)
            self.edge_weight[to].append((frm, weight))
        else:
            self.graph[to] = self.graph[to]

    def num_of_vertices(self):
        return len(self.vertices)

    def print_vertex(self):
        print(self.graph)

    def get_weight(self, frm, to):
        for v in self.edge_weight[frm]:
            if v[0] == to:
                weight = v[1]
        return weight

    def dfsUtil(self, s, visited, cache):
        # standard_weight = {}
        # for to in self.graph[s]:
        #     standard_weight[to] = self.get_weight(s, to)
        stack = []
        stack.append(s)
        visited[s] = True

        while stack:
            vertex = stack.pop()
            # if vertex in standard_weight:
            #     weight = standard_weight[vertex]
            # print(vertex, end=' ')
            cache.append(vertex)
            # traverse vertices adjacent to vertex
            for i in self.graph[vertex]:
                # if i in standard_weight:
                #     weight = standard_weight[i]
               if not visited[i]:
                    # if self.get_weight(vertex, i) == weight:
                        visited[i] = True
                        stack.append(i)

        # print()
    def eri_function(self, s, visited, cache):
        stack = []
        stack.append(s)
        visited[s] = True

        while stack:
            node = stack.pop()
            cache.append(node)
            for i in self.graph[node]:
                if not visited[i]:
                    if 'PLC' not in i:
                        visited[i] = True
                        stack.append(i)

    def dfs(self, s=None):
        cache = []
        visited = {i: False for i in self.graph}

        # traverse specified vertex
        if s is not None:
            self.dfsUtil(s, visited, cache)

        # traverse for all the vertices in other components of graph
        """ for v in self.graph:
            if not visited[v]:
                self.dfsUtil(v, visited, cache) """

        return len(cache)-1

    def eri_dfs(self, s=None):
        cache = []
        visited = {i: False for i in self.graph}

        if s is not None:
            self.eri_function(s, visited, cache)

        return len(cache)-1

    def cfs_calculate(self):
        cfs = {}
        total_number = self.num_of_vertices()
        for vertex in self.vertices:
            result = self.dfs(vertex)/total_number
            cfs[vertex] = result

        return cfs

    def eri_calculate(self):
        eri = {}
        total_number = self.num_of_vertices()
        for vertex in self.vertices:
            result = self.eri_dfs(vertex)/total_number
            eri[vertex] = result

        return eri

