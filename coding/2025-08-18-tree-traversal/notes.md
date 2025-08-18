# Tree Traversal Algorithms

This directory implements four classic traversal orders for a binary tree:

- **Pre‑order:** Visit the current node first, then recurse on the left and right subtrees.
- **In‑order:** Recurse on the left subtree, visit the node, then recurse on the right subtree.
- **Post‑order:** Recurse on the left and right subtrees, then visit the node.
- **Level‑order (BFS):** Visit nodes one level at a time using a queue.

## How It Works

A simple `TreeNode` class represents each node. Recursive functions perform the depth‑first traversals (pre/in/post), and a queue from `collections.deque` implements the breadth‑first traversal.

Example tree used in `solution.py`:

```
    1
   / \
  2   3
 / \
4   5
```

Traversals on this tree yield:

| Order      | Output          |
|-----------|-----------------|
| Pre‑order | [1, 2, 4, 5, 3] |
| In‑order  | [4, 2, 5, 1, 3] |
| Post‑order| [4, 5, 2, 3, 1] |
| Level‑order | [1, 2, 3, 4, 5] |

## Complexity Analysis

Let *n* be the number of nodes in the tree.

- **Time complexity:** Each traversal touches every node exactly once → **O(n)**.
- **Space complexity:** The call stack for the recursive traversals is at most the tree height (**O(h)**). Level‑order uses a queue storing up to *h* nodes at a time.

## Usage

Run `solution.py` directly. It constructs a sample tree and prints the results of each traversal. To adapt these functions to your own tree, import the functions and call them with your `TreeNode` root.
