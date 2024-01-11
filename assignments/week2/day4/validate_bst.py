def isValidBST(root):
    def check(root, l, r):
        if not root:
            return True

        elif l<root.val<r: 
            return check(root.left, l, root.val) and check(root.right,root.val,r)
        else:
            return False

    return check(root,-float('inf'),float('inf'))