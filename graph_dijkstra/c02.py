from heapq import heappop, heappush

'''Graph'''

graph = {0: [(__, 5), (5, 15), (8, 14)],
         1: [(0, 5), (2, 13), (5, 10), (9, 8)],
         2: [(1, 13), (3, __), (5, 4), (6, __), (2, 4)],
         3: [(2, 12), (4, 10), (6, 3), (9, 16)],
         4: [(__, 10), (6, 20), (7, 14)],
         5: [(0, 15), (1, 10), (__, 4), (6, 12), (7, 17), (8, 3)],
         6: [(2, 7), (3, 3), (4, 20), (5, 12), (7, 9), (8, 12)],
         7: [(4, 14), (5, __), (6, 9), (8, 19)],
         8: [(0, 14), (5, 3), (6, 12), (7, __)],
         9: [(__, 8), (2, 4), (3, 16)]
         }

'''Initialisation'''

num_nodes = len(graph)
priority_queue = [_______]
visited = [_____ for _ in range(num_nodes)]
distances = [float("inf") for _ in range(num_nodes)]
previous = [-1 for _ in range(num_nodes)]
distances[____] = _____

'''Main Algorithm'''

while ____________:

    dist, curr = heappop(priority_queue) 

    if not visited[curr]: 
        ______[curr] = True 

        for neighbour, weight in graph[______]:
            if not _______[_____] and weight + dist < _____[______]: 
                heappush(priority_queue, (_________, neighbour)) 
                distances[neighbour] = ________
                previous[neighbour] = ______

'''Path Calculation'''

dest = 4
print(distances[dest])
path, curr = [dest], dest
while previous[curr] != -1:
    curr = _______[curr]
    path.append(curr)
print(_______)