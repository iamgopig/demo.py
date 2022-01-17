class Graph:
    def init(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed
        if not directed:
            self.make_undirected()
    def make_undirected(self):
        for a in list(self.graph_dict.keys()):
            for (b, dist) in self.graph_dict[a].items():
                self.graph_dict.setdefault(b, {})[a] = dist
    def connect(self, A, B, distance=1):
        self.graph_dict.setdefault(A, {})[B] = distance
        if not self.directed:
            self.graph_dict.setdefault(B, {})[A] = distance
    def get(self, a, b=None):
        links = self.graph_dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)
    def nodes(self):
        s1 = set([k for k in self.graph_dict.keys()])
        s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
        nodes = s1.union(s2)
        return list(nodes)
class Node:
    def init(self, name: str, parent: str):
        self.name = name
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0
    def eq(self, other):
        return self.name == other.name
    def lt(self, other):
        return self.f < other.f
    def repr(self):
        return ('({0},{1})'.format(self.name, self.f))
def astar_search(graph, heuristics, start, end):
    open = []
    closed = []
    start_node = Node(start, None)
    goal_node = Node(end, None)
    open.append(start_node)
    while len(open) > 0:
        open.sort()
        current_node = open.pop(0)
        closed.append(current_node)
        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node.name + ': ' + str(current_node.g))
                current_node = current_node.parent
            path.append(start_node.name + ': ' + str(start_node.g))
            return path[::-1]
        neighbors = graph.get(current_node.name)
        for key, value in neighbors.items():
            neighbor = Node(key, current_node)
            if (neighbor in closed):
                continue
            neighbor.g = current_node.g + graph.get(current_node.name, neighbor.name)
            neighbor.h = heuristics.get(neighbor.name)
            neighbor.f = neighbor.g + neighbor.h
            if (add_to_open(open, neighbor) == True):
                open.append(neighbor)
    return None
def add_to_open(open, neighbor):
    for node in open:
        if (neighbor == node and neighbor.f > node.f):
            return False
    return True
def main():
    graph = Graph()
    graph.connect('A', 'B', 6)
    graph.connect('A', 'F', 3)
    graph.connect('F', 'G', 1)
    graph.connect('F', 'H', 7)
    graph.connect('B', 'D', 2)
    graph.connect('B', 'C', 3)
    graph.connect('D', 'C', 1)
    graph.connect('D', 'E', 8)
    graph.connect('C', 'E', 5)
    graph.connect('E', 'I', 5)
    graph.connect('E', 'J', 5)
    graph.connect('I', 'J', 3)
    graph.connect('G', 'I', 3)
    graph.connect('H', 'I', 2)
    graph.make_undirected()
heuristics = {}
heuristics['A'] = 10
heuristics['B'] = 8
heuristics['C'] = 5
heuristics['D'] = 7
heuristics['E'] = 3
heuristics['F'] = 6
heuristics['G'] = 5
heuristics['H'] = 3
heuristics['I'] = 1
heuristics['J'] = 0

# Run the search algorithm
path = astar_search(Graph, heuristics, 'A', 'J')
print(path)
print()
# Tell python to run main method
if __name__ == "main": main()