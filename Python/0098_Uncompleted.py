class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def percorreArvore(self, node):
        if node.right is not None:
            if node.right.val <= node.val:
                return False
            return self.percorreArvore(node.right)
        if node.left is not None:
            if node.left.val >= node.val:
                return False
            return self.percorreArvore(node.left)
        return True

    def isValidBST(self, root: TreeNode) -> bool:
        return self.percorreArvore(root)
