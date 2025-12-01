def count_power_groups(stations, lines):
    """
    Given a list of station names and a list of undirected connections (lines),
    return how many connected groups exist.
    """

    # Build adjacency list
    graph = {s: [] for s in stations}

    for a, b in lines:
        graph[a].append(b)
        graph[b].append(a)

    visited = set()
    groups = 0

    # DFS to explore each component
    def dfs(start):
        stack = [start]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        stack.append(neighbor)

    # Count connected components
    for station in stations:
        if station not in visited:
            dfs(station)
            groups += 1

    return groups


if __name__ == "__main__":
    # Optional manual test
    stations = ["A", "B", "C", "D"]
    lines = [("A", "B"), ("B", "C")]
    print(count_power_groups(stations, lines))  # Expected: 2
