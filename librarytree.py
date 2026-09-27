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

    book_title = input("Enter book/category name (-1 to exit)\n:")

    if book_title == "-1":
        return None

    root = Node(book_title)

    print(f"Enter left sub-category of '{book_title}'")
    root.left = create()

    print(f"Enter right sub-category of '{book_title}'")
    root.right = create()

    return root

def main():

    print("--- Library Catalog Navigation ---")
    print("Build the catalog tree: each node is a book/category,")
    print("left = one branch of sub-categories, right = another branch.\n")

    root = create()

    preorderset = []
    preorder(root,preorderset)

    inorderset = []
    inorder(root,inorderset)

    postorderset = []
    postorder(root,postorderset)

    print(f"\nPreorder Catalog Scan:{preorderset}")
    print(f"Inorder Catalog Scan:{inorderset}")
    print(f"Postorder Catalog Scan:{postorderset}")

main()