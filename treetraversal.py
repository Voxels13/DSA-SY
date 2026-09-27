class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def preorder(node,dataset):

    if node == None:
        return

    dataset.append(node.data)

    preorder(node.left,dataset)

    preorder(node.right,dataset)

def inorder(node,dataset):

    if node == None:
        return

    inorder(node.left,dataset)

    dataset.append(node.data)

    inorder(node.right,dataset)
    

def postorder(node,dataset):

    if node == None:
        return

    postorder(node.left,dataset)

    postorder(node.right,dataset)

    dataset.append(node.data)


def create():

    nodeval = int(input("Enter node value (-1 to exit)\n:"))

    if nodeval == -1:
        return None

    root = Node(nodeval)

    print(f"Enter left value of {nodeval}")
    root.left = create()

    print(f"Enter right value of {nodeval}")
    root.right = create()

    return root

def main():

    root = create()

    preorderset = []
    preorder(root,preorderset)

    inorderset = []
    inorder(root,inorderset)

    postorderset = []
    postorder(root,postorderset)

    print(f"Preorder:{preorderset}")
    print(f"Inorder:{inorderset}")
    print(f"Postorder:{postorderset}")

main()