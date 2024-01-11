def invertTree(root):        
    if not root:
        return root

    root.right, root.left = root.left, root.right
    invertTree(root.left)
    invertTree(root.right)
    return root