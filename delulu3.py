from heapq import *
class TreeMap:
    def __init__(self, roads, solulus):
        
        self.solulus = solulus
        max = 0
        for i in roads:
            if max < i[0]:
                max = i[0]
            if max < i[1]:
                max = i[1]
        self.trees = [[]] * (max + 1)
        for i in range(len(self.trees)):
            self.trees[i] = []
            self.trees[i].append(i)
        for i in range(len(roads)):
            self.trees[roads[i][0]].append((roads[i][1], roads[i][2]))
        
       
        

    def escape(self, start, exits):
        a = dijkstra(self.trees, start)
        self.trees.append([len(self.trees)])
        for i in self.solulus:
            self.trees[len(self.trees) - 1].append((i[2], i[1] + a[0][i[0]]))
        b = dijkstra(self.trees, len(self.trees) - 1)
        self.trees.pop()

        max = (float('inf'), "null")
        for i in exits:
            if b[0][i] < max[0]:
                max = (b[0][i], i)
        order = list()
        cur = max[1]
        print(a, b)
        while cur != len(self.trees):
            order.append(cur)
            cur = b[1][cur]

        print(order)
        
        cur = order[len(order) - 1]
        for i in self.solulus:
            if i[2] == order[len(order) - 1]:
                cur  = i[0]
                break
        while a[0][cur] != 0:
            cur = a[1][cur]
            order.append(cur)
        order.reverse()

        return (max[0], order)
    

        

def dijkstra(graph, source) -> tuple:
    dist = [float('inf')] * len(graph)
    pred = [0] * len(graph)
    dist[source] = 0
    prioirtyQueue = [-1] * len(graph)
    for i in range(len(graph)):
        prioirtyQueue[i] = (dist[i], i)
    heapify(prioirtyQueue)
    while len(prioirtyQueue) > 0:
        current = heappop(prioirtyQueue)[1]
        for i in range(1,len(graph[current])):
            if len(graph[current]) != 1:
                vertexTo = graph[current][i][0]
                weight = graph[current][i][1]
                relax(current, vertexTo, weight, dist, pred, prioirtyQueue)
    return dist, pred

    
def relax(u, v, weight, dist, pred, queue) -> None:
    if (dist[v] > dist[u] + weight):
        dist[v] = dist[u] + weight
        heappush(queue, (dist[v], v))
        pred[v] = u

b =  [(0,1,4), (1,2,2), (2,3,3), (3,4,1), (1,5,2),
        (5,6,5), (6,3,2), (6,4,3), (1,7,4), (7,8,2),
        (8,7,2), (7,3,2), (8,0,11), (4,3,1), (4,8,10)]

tree = TreeMap(b,  [(5,10,0), (6,1,6), (7,5,7), (0,5,2), (8,4,8)])
print(tree.escape(1, [3, 4]))
a = [(0, (1,1), (2,3)), (1,(2,1)), (2,(3,1)), (3,(5,1)), (4,(5,1)), (5,)]
#print(dijkstra(a, 0))




