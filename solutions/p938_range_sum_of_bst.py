# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        vals =  inorder(root, [])
        total = 0
        for val in vals:
            if L <= val and val <= R:
                total += val
        return total
def inorder(root, vals):
    if root:
        vals.append(root.val)
        inorder(root.left, vals)
        inorder(root.right, vals)
    return vals
