from typing import DefaultDict
import sys
sys.setrecursionlimit(10**6)

answer = 0


def solution(a, edges):
    if sum(a) != 0:
        return -1
    global answer
    tree = DefaultDict(list)
    for l_node, r_node in edges:
        tree[l_node].append(r_node)
        tree[r_node].append(l_node)
    visited = [0] * len(a)

    def dfs(par):
        global answer
        visited[par] = 1
        for child in tree[par]:
            if not visited[child]:
                a[par] += dfs(child)
        answer += abs(a[par])
        return a[par]
    
    if dfs(0) != 0:
        return -1
    return answer