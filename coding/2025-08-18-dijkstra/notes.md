# Notes for Dijkstra's Algorithm

**Problem:** Given a weighted directed graph (non‑negative weights) with `n` nodes and `m` edges, compute the shortest distance from a source node to all other nodes.

**Approach:**

- Build an adjacency list to store outgoing edges for each node.
- Initialize all distances to infinity and set the source distance to 0.
- Use a min‑priority queue (min‑heap) to repeatedly pick the node with the smallest known distance.
- For each outgoing edge from the popped node, **relax** the edge: if the new path distance is smaller than the current stored distance, update it and push the neighbor into the heap.
- Skip outdated entries popped from the heap (lazy deletion) since they no longer represent the best known distance.

**Complexity:**

For a graph with `n` nodes and `m` edges, Dijkstra's algorithm runs in `O((n + m) \log n)` time using a binary heap and uses `O(n + m)` space for the adjacency list and distance array.

**Example test:**

```
5 6
0 1 10
0 2 3
1 2 1
2 1 4
2 3 2
3 4 9
0
```

Starting from node 0, the expected distances are:

- Node 0: 0
- Node 1: 7 (0→2→1)
- Node 2: 3 (0→2)
- Node 3: 5 (0→2→3)
- Node 4: 14 (0→2→3→4)

**What I learned:**

Dijkstra's algorithm efficiently handles graphs with non‑negative weights. Using a priority queue ensures that each node's shortest distance is processed exactly when it becomes optimal, giving a near‑linear time complexity in practice for sparse graphs.
