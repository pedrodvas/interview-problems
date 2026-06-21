# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        print(root.val, root.left, root.right)
        '''going up a node, there are some options:
        we use the left sum, and then go up
        we use the right sum, and then go left
        we lock an arc

        but if we want to use that node on sums
        that will come up later, we need to pass
        the bigger sum between the left and right
        paths.
        '''

        max_sum = [-float('inf')]
        rec_max_path_sum(root, max_sum)

        return max_sum[0]

def rec_max_path_sum(root, max_sum):
    if root == None:
        return 0
    sum_left = max(0, rec_max_path_sum(root.left, max_sum))
    sum_right = max(0, rec_max_path_sum(root.right, max_sum))
    sum_node = root.val

    if max_sum[0] < sum_left + sum_node + sum_right:
        max_sum[0] = sum_left + sum_node + sum_right
    
    return max(0, sum_left, sum_right)+sum_node

if __name__ == "__main__":
    sol = Solution()