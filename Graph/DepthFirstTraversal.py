# Program to perform depth first traversal in a graph
from collections import defaultdict
import xlwt
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

def metrics_save(file_name, metrics):                # 将计算结果保存到xls文件中
    temp_list = [('节点名称', 'CFS')]
    for metric in metrics:
        temp_list.append((metric, metrics[metric]))

    file = xlwt.Workbook()
    sheet1 = file.add_sheet('sheet1', cell_overwrite_ok=True)
    style = xlwt.XFStyle()
    al = xlwt.Alignment()
    al.vert = 0x01
    al.horz = 0x02
    style.alignment = al

    for i in range(len(temp_list)):
        for j in range(len(temp_list[i])):
            sheet1.write(i, j, temp_list[i][j], style)
    file.save(file_name)

def save_all_metrics(file_name, metrics):
    metrics_list = defaultdict(list)
    temp_list = [('节点名称', 'CFS', 'ERI')]
    for metric in metrics:
        for i in metric:
            metrics_list[i].append(metric[i])
    for i in metrics_list:
        temp_list.append((i, metrics_list[i][0], metrics_list[i][1]))

    file = xlwt.Workbook()
    sheet1 = file.add_sheet('sheet1', cell_overwrite_ok=True)
    style = xlwt.XFStyle()
    al = xlwt.Alignment()
    al.vert = 0x01
    al.horz = 0x02
    style.alignment = al

    for i in range(len(temp_list)):
        for j in range(len(temp_list[i])):
            sheet1.write(i, j, temp_list[i][j], style)
    file.save(file_name)



""" if __name__ == '__main__':
    # make an undirected graph
    graph = Graph()

    # component 1 of the graph
    graph.addEdge(0, 1)
    graph.addEdge(0, 2)
    graph.addEdge(1, 2)
    graph.addEdge(2, 3)
    graph.addEdge(3, 3)
    graph.addEdge(1, 4)
    graph.addEdge(1, 5)
    graph.addEdge(3, 6)

    # component 2 of the graph
    graph.addEdge(7, 8)
    graph.addEdge(8, 9)
    graph.addEdge(7, 10)

    # call dfs from 2 vertex
    print("Depth First Traversal:")
    graph.dfs(2) """