def dfs(nodes):
    routes = []
    stack = ['ICN']
    while stack:
        top = stack[-1]
        if (top not in nodes) or (not nodes[top]):
            routes.append(stack.pop())
        else:
            stack.append(nodes[top].pop())
    return routes[::-1]


def solution(tickets):
    nodes = {}
    for origin, destination in tickets:
        nodes[origin] = nodes.get(origin, []) + [destination]

    for origin in nodes:
        nodes[origin].sort(reverse=True)

    return dfs(nodes)

if __name__ == "__main__":
    # tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
    # tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
    tickets = [["ICN", "JFK"], ["ICN", "ATL"], ["JFK", "ICN"]]
    print(solution(tickets))