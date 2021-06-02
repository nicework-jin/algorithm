# 시간/효율성 향상 글 정리: https://gaza-anywhere-coding.tistory.com/140
import sys
sys.setrecursionlimit(10000)
sys.stdin = open('input.txt', 'r')

INPUT = sys.stdin.readline


def dfs(i, graph, visited, vertex_num):
    visited[i] = True
    for j in range(1, vertex_num + 1):
        if visited[j]:
            continue
        if graph[i][j] == 0:
            continue
        dfs(j, graph, visited, vertex_num)


def solution():
    vertex_num, edges_num = map(int, INPUT().split())
    graph = [[0] * (vertex_num + 1) for i in range((vertex_num + 1))]
    visited = [0] * (vertex_num + 1)

    for i in range(edges_num):
        a, b = map(int, INPUT().split())
        graph[a][b] = 1
        graph[b][a] = 1

    cnt = 0
    for i in range(1, vertex_num + 1):
        if visited[i] == 0:
            cnt += 1
            dfs(i, graph, visited, vertex_num)
    return cnt
print(solution())
