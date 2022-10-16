class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def percorreArvore(self, node, array):
        if node.left is not None:
            self.percorreArvore(node.left, array)
        array.append(node.val)
        # if len(array) > 1 and array[len(array) - 2] >= array[-1]:
        #     print(array[len(array) - 2], array[-1])
        #     return array
        if node.right is not None:
            self.percorreArvore(node.right, array)
        return array

    def isValidBST(self, root: TreeNode):
        array = self.percorreArvore(root, [])
        i = 0
        while i + 1 < len(array):
            if array[i] >= array[i + 1]:
                return False
            i += 1

        return True


root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(6)
root.right.left = TreeNode(3)
root.right.right = TreeNode(7)

print(Solution().isValidBST(root))
