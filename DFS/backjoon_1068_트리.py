import sys
INPUT = sys.stdin.readline


def remove_node(tree, parents, n):
    """ 요청받은 노드를 제거 합니다.

    1. tree 내에 자신(n)을 자식으로 나타내는 부모 노드에서 n을 지웁니다.
      -> parents[n] == -1은 루트 노드이므로 부모 노드가 없습니다.
    2. 재귀적으로 자식 노드를 지웁니다. 지워진 자식 노드의 tree 내에 값을 [-1]로 표기합니다.
    """
    if parents[n] != -1:
        tree[parents[n]].remove(n)

    def remove_child(x):
        for i in tree[x]:
            remove_child(i)
        tree[x] = [-1]
    remove_child(n)


def solution():
    """ 자식이 없는 노드의 개수를 출력합니다.

    1. 이중 리스트(tree)를 생성하고 자신의 자식 노드 인덱스를 넣습니다.
      -> 문제에서 주어진 값 중 -1은 부모 노드가 없음을 의미합니다.
    2. 문제에서 주어진 노드를 제거합니다.
    3. tree에서 자식이 없는 노드([], 빈 노드)의 개수를 출력합니다.
    """
    node_num = int(INPUT())
    parents = list(map(int, INPUT().split()))
    tree = [[] for _ in range(node_num)]

    for i in range(node_num):
        if parents[i] == -1:
            continue
        tree[parents[i]].append(i)

    remove_node(tree, parents, node_to_remove := int(INPUT()))
    return tree.count([])

if __name__ == '__main__':
    print(solution())
