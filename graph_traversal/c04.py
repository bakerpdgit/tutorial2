from collections import deque

'''Graph'''

graph = {
    1: [2, __, 9],
    2: [1, 6],
    3: [__, 4, 8],
    4: [3, 5, __],
    5: [4, 11],
    6: [2, __, 8, 10],
    7: [__, 11],
    8: [3, 6],
    9: [__],
    10: [6, 7],
    11: [5, __, 12],
    12: [__]
}

'''Main Algorithm'''

def bfs(graph, start):

    queue = deque([______])
    visited = set()
    path = []
    
    while queue:

        curr = queue.popleft()

        if curr not in _____:

            path.append(______)
            ______.add(curr)

            for neighbour in _____[curr]:
                if _____ not in visited:
                    _______.append(neighbour)
    
    return path

print(bfs(graph, 1))
