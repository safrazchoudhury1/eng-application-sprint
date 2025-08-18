import sys
import heapq


def dijkstra(n, edges, start):
    """Compute shortest paths from start to all nodes using Dijkstra's algorithm.

    Args:
        n (int): number of nodes labeled 0..n-1
        edges (list[tuple[int,int,float]]): list of directed weighted edges (u, v, w)
        start (int): source node index

    Returns:
        list[float]: distances from start to each node (inf if unreachable)
    """
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
    dist = [float("inf")] * n
    dist[start] = 0.0
    heap = [(0.0, start)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))
    return dist


def main():
    """Read graph from stdin and print shortest distances.

    Expected input format:
        n m
        u1 v1 w1
        u2 v2 w2
        ...
        um vm wm
        start

    Nodes are 0-indexed. Weights can be integers or floats.
    """
    data = sys.stdin.read().split()
    if not data:
        print("Usage: provide n m then m lines of u v w and a start index.")
        return
    it = iter(data)
    try:
        n = int(next(it))
        m = int(next(it))
    except StopIteration:
        print("Invalid input.")
        return
    edges = []
    for _ in range(m):
        try:
            u = int(next(it))
            v = int(next(it))
            w = float(next(it))
        except StopIteration:
            print("Invalid edge input.")
            return
        edges.append((u, v, w))
    try:
        start = int(next(it))
    except StopIteration:
        print("Missing start vertex.")
        return
    dist = dijkstra(n, edges, start)
    for i, d in enumerate(dist):
        if d == float("inf"):
            print(f"{i}: INF")
        else:
            print(f"{i}: {d}")


if __name__ == "__main__":
    main()
