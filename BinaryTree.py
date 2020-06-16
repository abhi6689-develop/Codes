class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 

class Binarytree:
    def __init__(self,root):
        self.root = Node(root)
#depth-first searches 
    def preorder(self, start, traversal):
        if start != None:
            traversal += (str(start.data)+"->") #prints the starting node 
            traversal = self.preorder(start.left, traversal) #checks for the left node, if there makes it the start, prints it, and check if the left node has left nodes.  
            traversal = self.preorder(start.right, traversal) #check for the right node, if there makes it the head, prints it, and checks if it has left subnodes. 
        return traversal
    
    def inorder(self, start, traversal):
        if start != None:
            traversal = self.inorder(start.left, traversal)#travles to the last left node, makes it the start.
            traversal += (str(start.data)+"->") #prints it 
            traversal = self.inorder(start.right, traversal) #v 
        return traversal
    
    def postorder(self, start, traversal):
        if start != None:
            traversal = self.postorder(start.left, traversal)
            traversal = self.postorder(start.right, traversal)
            traversal += (str(start.data)+"->")
        return traversal

#breadth-first searches
        
    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder(tree.root, "Pre-order traversal: ")
        elif traversal_type == "inorder":
            return self.inorder(tree.root, "Inorder traversal: ")
        else:
            return self.postorder(tree.root, "Post-order traversal: ")

        
tree = Binarytree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
print(tree.print_tree("preorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("post"))