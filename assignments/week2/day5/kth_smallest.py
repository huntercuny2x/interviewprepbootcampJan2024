def kthSmallest(root, k):
    stack = []
    
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root=stack.pop()
        k-=1
        if k == 0:
            return root.val
        root=root.right