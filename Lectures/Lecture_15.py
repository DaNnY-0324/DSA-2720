# BST Implementation

class BST:
    def __init__(self):
        self.root = None

    def insert(self, x):
        p = Node(x)
        if self.root is None:
            self.root = p
        else:
            q = self.root
            while True:
                if ( p.val < q.val):
                    if q.left is None:
                        q.left = p
                        break
                    else:
                        q=q.left
                        continue
                else: 
                    if q.right is None:
                        q.right = p
                        break
                    else:
                        q = q.right 
                        continue
    
    def treeMIN(self):
        if self.root is None:
                return None
        else:
            q = self.root
            while (q.left is not None):
                q=q.left
            return q
        
    def parent(self,x):
        if self.root is None or self.root == x :
            return None        
        p = self.root
        while True:
            if (x.val < p.val):
                if p.left == x:
                    return p
                else:
                    p = p.left
            else:
                if p.right == x:
                    return p
        else:
            p = p.right

    def successor(self, r):    
        if self.root is None or r == treeMAX(self):
            return None
        if r.right is not None:
            return treeMIN(r.right)
            
        pass

class Node: 
    def __init__(self,x):
        self.left = None
        self.right = None
        self.val = x
        
# Main Function
bst = BST()
bst.insert(12)
bst.insert(8)
bst.insert(16)
bst.insert(10)
bst.insert(13)
bst.insert(9)
bst.insert(14)
p = bst.parent(x)
s = bst.succ(r)

