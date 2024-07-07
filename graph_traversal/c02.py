'''Graph'''

graph = {
    1: [__, 6],
    2: [8, 10],
    3: [1, __, 10, __],
    4: [10],
    5: [9, 11],
    6: [1],
    7: [__, 8],
    8: [2, 7, __, 11],
    9: [5, __, 10],
    10: [__, 3, 4, 9],
    11: [3, 5, __, 12],
    12: [11]
}

'''Main Algorithm'''

def dfs(graph, curr, visited=set()):

    path = [curr]
    ______.add(_____)

    for neighbour in _____[_____]:
        if ______ not in visited:
            _____.extend(dfs(graph, _____, _____))

    return ____

print(dfs(graph, 1))
