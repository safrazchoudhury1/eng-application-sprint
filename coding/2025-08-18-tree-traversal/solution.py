from collections import deque


class TreeNode:
    """Binary tree node for traversal algorithms."""

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder(root):
    """Return a list of values from a preorder traversal."""
    if root is None:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)


def inorder(root):
    """Return a list of values from an inorder traversal."""
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def postorder(root):
    """Return a list of values from a postorder traversal."""
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]


def level_order(root):
    """Return a list of values from a breadth‑first (level order) traversal."""
    if root is None:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


def build_sample_tree():
    """Build a sample tree for demonstration.
    The structure is:
            1
           / \
          2   3
         / \   
        4   5
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    return root


if __name__ == "__main__":
    # Demonstrate traversals on the sample tree
    tree = build_sample_tree()
    print("Preorder:", preorder(tree))
    print("Inorder:", inorder(tree))
    print("Postorder:", postorder(tree))
    print("Level order:", level_order(tree))
