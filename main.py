import sys

sys.setrecursionlimit(100000)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxPathSum(root):
    max_sum = float("-inf")

    def dfs(node):
        nonlocal max_sum

        if node is None:
            return 0

        left_gain = max(dfs(node.left), 0)
        right_gain = max(dfs(node.right), 0)

        current_path_sum = node.val + left_gain + right_gain

        max_sum = max(max_sum, current_path_sum)

        return node.val + max(left_gain, right_gain)

    dfs(root)

    return max_sum


# Приклад 1
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)

print("Приклад 1:", maxPathSum(root1))


# Приклад 2
root2 = TreeNode(-10)
root2.left = TreeNode(9)
root2.right = TreeNode(20)
root2.right.left = TreeNode(15)
root2.right.right = TreeNode(7)

print("Приклад 2:", maxPathSum(root2))


# Додатковий приклад
root3 = TreeNode(-3)

print("Приклад 3:", maxPathSum(root3))