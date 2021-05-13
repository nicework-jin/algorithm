"""
프로그래머스, 네트워크
  A B C D
A 1 1 0 1  가로 방향으로 한 줄씩 탐색하며, 1을 만나면 해당 노드를 호출한 뒤 방문처리.  
B 1 1 0 0   이를 A~D에 반복적으로 수행하면 하나의 네트워크에 연결된 노드에 방문하면, 연결된 모든 노드를 방문할 수 있음.
C 0 0 1 0   
D 1 0 0 1   
"""


def dfs(computers, visited, k):
    visited[k] = 1
    for i in range(len(computers)):
        if computers[k][i] == 1 and visited[i] == 0:
            dfs(computers, visited, i)


def solution(n, computers):
    visited = [0] * n
    cnt = 0
    for i in range(n):
        if visited[i] == 0:
            dfs(computers, visited, i)
            cnt += 1
    return cnt

if __name__ == '__main__':
    n = 3
    computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(solution(n, computers))
