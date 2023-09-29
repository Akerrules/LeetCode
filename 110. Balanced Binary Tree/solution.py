def isBalanced(self, root: Optional[TreeNode]) -> bool:
    
    #find height of left tree and right tree and compare
    if(root == None):
        return True
    def height(node) -> int:
        if(node is None):
            return 0
        return max(height(node.left), height(node.right)) + 1
    left_h = height(root.left)
    right_h = height(root.right)
    
    print(left_h, right_h)

    return (abs(left_h-right_h)<2) and self.isBalanced(root.left) and self.isBalanced(root.right)


