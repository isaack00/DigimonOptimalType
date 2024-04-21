
def fuse(pokemon):
    """
		Function description: This function returns an output integer containing the largest possible combination of a fusemon in an order given

		Approach description: This is a dynamic programming problem. The approach was to essentailly have it that any given combination of a fitmon is the best combination, eg ABC and DE combine, this will be the best combination of ABC not just any ABC.
        It continualy uses the best combination obtained when combining elements. Eg (a(bc)) and (ab(c)) are two combos that both result in abc, this dynamic programming solution will only take the best of those two when taking into consdiertions that use abc.

		Input: 
			pokemon: an array based list containing lists of size three, in which postion 0 and 2 is a float between 0.1 and 0.9 (inclusive), and position one is an integer, positive
		
		Output: an integer that represtent the optimal order combination that can be achieved when fusing pokemon
		
		Time complexity: O(n^3), where n is the amount of elements in the pokemon list

		Time complexity analysis : No search or sort algorthims are here, so the time complexity is purerly its own. While the first loop is the size of the list -1, (n)
        it contains a for loop that is n - index1 (index pf first loop), this is a constant, so therefore its n. the third for loop is also n, while slightly less than n in reality, would simplify to n given infinitely large solutions.
        (n-1)*(n*logn)*(n*logn) = n^3

		Space complexity: O(n^2),  where n is the number of elements in the pokemon (input) array

		Space complexity analysis: A table is created that uses the the pokemon input array and squares it, therefore n*n = n^2
		
	"""


    table = [[0 for _ in range(len(pokemon))] for _ in range(len(pokemon))]
    for i in range(len(table)):
        table[i][i] = pokemon[i]
    for diagonal in range(1, len(table)):
        for i in range(len(table) - diagonal):
            max = [0,0,0]
        
            for k in range(diagonal):
            
                if max[1] < table[i][k + i][2]*table[i][k + i][1] + table[i+k +1][diagonal + i][0]*table[i+k + 1][diagonal+ i][1]:
                    max = [table[i][k + i][0], int(table[i][i+k][2]*table[i][i+k][1] + table[i+k+1][diagonal+i][0]*table[i+1+k][diagonal+i][1]), table[1+i+k][diagonal+i][2]]
        
            table[i][i + diagonal] = max
        
        
    return table[0][len(table) -1][1]
    
    


from heapq import *
class TreeMap:
    
    def __init__(self, roads, solulus):
        """
		Function description: This function creates an instance of a treemap, which consits of a list of elements, each represtning a node, in these elemnts, the node integer is always the first element, followed by the edges it contains

		Approach description: The approach was to transform from each element represtening an edge to each element represtning a node. This was done by finding the biggest node by looking at all elements from the orgrinal list, then using to create a node base list

		Input: 
			roads: list of eleemnts containing edges represtned by tuples: (node, node destination, weight)
            solulus: list of elements contiaining tuples that are meant to be solulut trees: (node, destroy time, teleport location)
		
		Output: none
		
		Time complexity: o(r + n) where r is the size of roads and n is nodes

		Time complexity analysis : the initial for loop to find the biggest node is size n, as it cycles through all roads. then, the for loops cycling through self.tree is cycling through the nodes in the graph, therefore o(n) where n is nodes
        Therefore: o(r)+o(n)+o(r) = o(r+n), r is roads, n is nodes

		Space complexity: o(n+r) where n is nodes and r is roads

		Space complexity analysis: when self.solulus is created that is at max o(n) where n is nodes, self.trees while appearing to be o(n) is not, 
        as it contians all the nodes (o(n)) but also all roads (o(r)), therefore o(r+n). o(n) + o(r+n) = o(r+n) where n is nodes and r is roads
		
	    """
        
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
        """
		Function description: Find the fastest way to an exit given that a solulu has been destroyed, from a starting point

		Approach description: Dikstra to each node, take the values for the each solulu. Create a sink point for the same graph, then that sink point connects to where teh solulu teleports you to with the weight of how much getting to that solulu cost. Dijstra from that sink point to all nodes and find the biggest out of the exits.
		Input: 
			start: int that reprresntens node to start from in the search for esacpe
            exit: list of exits in the graph
		
		Output: tuple contiaining the amount of time taken to optimally escape as well as the path taken in said escape
		
		Time complexity: o(r*logn) where r is roads and n is nodes

		Time complexity analysis : each dijstra is o(r*logn). The for loop for solulus is at most o(n), as with the exits and the while loops.
        Therefore o(r*logn) + o(n)*4 = o(r*logn + n) of course r dominates n, so therefore o(r*logn) where n is node and r is roads

		Aux Space complexity: o(n) where n is nodes

		Aux Space complexity analysis: lists are created with size of the nodes in the graph, these are firstSearch and secondSearch. order has a maximum size of the size of nodes in the graph
        therefore o(n) * 3 = o(n)
		
	"""
        firstSearch = dijkstra(self.trees, start)
        self.trees.append([len(self.trees)])
        for i in self.solulus:
            self.trees[len(self.trees) - 1].append((i[2], i[1] + firstSearch[0][i[0]]))
        secondSearch = dijkstra(self.trees, len(self.trees) - 1)
        self.trees.pop()

        max = (float('inf'), "null")
        for i in exits:
            if secondSearch[0][i] < max[0]:
                max = (secondSearch[0][i], i)
        order = list()
        cur = max[1]
        if cur == 'null':
            return None
        while cur != len(self.trees):
            order.append(cur)
            
            cur = secondSearch[1][cur]
        cur = order[len(order) - 1]
        for i in self.solulus:
            if i[2] == order[len(order) - 1]:
                cur  = i[0]
                break
        while firstSearch[0][cur] != 0:
            cur = firstSearch[1][cur]
            order.append(cur)
        order.reverse()
        
        return (max[0], order)
    

        

def dijkstra(graph, source) -> tuple:
    """
		Function description: Dijstras algrothim using a min heap

		Approach description: design an dijstras that uses a min heap for a more effieicent time
		Input: 
			graph: list of elements that contain list with the structurer of the first eleemnt being the node number and the following elements being as many edges as there are
            source: the starting node
		
		Output: list of size nodes in which each element represtnet the fastest time to that node, and a list of eleemnts that is used to determine the path taken to get to said eleemtn the fastest way 
		
		Time complexity: o(e*logn) where e is edges and n is nodes

		Time complexity analysis : while loop is o(n), removing element is o(logn) where n is nodes. each edge is visted o(e), updating min heap is o(logn), where e is edges and n is nodes. 
        Therefore: o(e*logn+n*logn) = o(e*logn), since edges dominate nodes, where n is nodes and e is edges

		Aux Space complexity: o(n) where n is nodes in graph (size of graph in this case)

		Aux Space complexity analysis: three lists created both with the size of how many nodes there are. therefore o(n) +o(n)+o(n) = o(n) where n is nodes
		
	"""
    dist = [float('inf')] * len(graph)
    pred = [0] * len(graph)
    dist[source] = 0
    heap = [-1] * len(graph)
    for i in range(len(graph)):
        heap[i] = (dist[i], i)
    heapify(heap)
    while len(heap) > 0:
        current = heappop(heap)[1]
        for i in range(1,len(graph[current])):
            if len(graph[current]) != 1:
                vertexTo = graph[current][i][0]
                weight = graph[current][i][1]
                relax(current, vertexTo, weight, dist, pred, heap)
    return dist, pred

    
def relax(u, v, weight, dist, pred, heap) -> None:

    """
		Function description: perform edge relaxtion for dijstra

		Approach description: update the paths if there is a new smaller path
		Input: 
            u: vertex 1 for given edge
            v: vertext 2 for given edge
            weight: weight for edge
            dist: list containing the current paths known
            pred: the list that contains the current routes for each node
            heap: min heap represtning order of shortets paths
			
		
		Output: none, rather it edits the lists
		
		Time complexity: o(logn) where n is length of heap

		Time complexity analysis : since everything is o(1) except heappush, which is o(logn)

		Space complexity: o(1)

		Space complexity analysis: nothing new created
		
	"""

    if dist[v] > dist[u] + weight:
        dist[v] = dist[u] + weight
        heappush(heap, (dist[v], v))
        pred[v] = u

