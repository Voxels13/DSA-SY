class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def preorder(root,dataset):

    if root == None:
        return dataset

    dataset.append(root.data)

    preorder(root.left,dataset)

    preorder(root.right,dataset)

    return dataset

def inorder(root,dataset):

    if root == None:
        return dataset

    inorder(root.left,dataset)

    dataset.append(root.data)

    inorder(root.right,dataset)

    return dataset

def postorder(root,dataset):

    if root == None:
        return dataset

    postorder(root.left,dataset)

    postorder(root.right,dataset)

    dataset.append(root.data)

    return dataset


def insert(root,roll_no):

    if root == None:
        return Node(roll_no)

    if roll_no < root.data:
        root.left = insert(root.left,roll_no)
    elif roll_no > root.data:
        root.right = insert(root.right,roll_no)
    else:
        print(f"Roll No {roll_no} already exists, skipping duplicate.\n")

    return root


def search(root,roll_no):

    if root == None:
        return False

    if root.data == roll_no:
        return True
    elif roll_no < root.data:
        return search(root.left,roll_no)
    else:
        return search(root.right,roll_no)


def createtree(nodeset):

    if not nodeset:
        return None

    root = None

    for roll_no in nodeset:
        root = insert(root,roll_no)

    return root


def main():

    print("--- Student Admission Record Management ---\n")

    n = int(input("Enter number of admission records: "))

    values = input("Enter roll numbers: ").split()
    values = [int(v) for v in values]

    if n == len(values):
        root = createtree(values)

        preorderset = []
        preorder(root,preorderset)
        print("Preorder :",*preorderset)

        inorderset = []
        inorder(root,inorderset)
        print("Inorder (sorted roll numbers) :",*inorderset)

        postorderset = []
        postorder(root,postorderset)
        print("Postorder :",*postorderset)

        #Sample search demonstration
        search_roll = int(input("\nEnter roll number to search: "))
        if search(root,search_roll):
            print(f"Roll No {search_roll} found in admission records.")
        else:
            print(f"Roll No {search_roll} not found in admission records.")

    else:
        raise ValueError("Invalid Length for values")

main()