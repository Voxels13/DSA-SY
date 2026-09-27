class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LibraryCatalog:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_at_beginning(self, book):
        new_node = Node(book)
        new_node.next = self.head
        self.head = new_node
        print(f"'{book}' inserted at the beginning.")

    # Insert at end
    def insert_at_end(self, book):
        new_node = Node(book)

        if self.head is None:
            self.head = new_node
            print(f"'{book}' inserted at the end.")
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        print(f"'{book}' inserted at the end.")

    # Delete from beginning
    def delete_from_beginning(self):
        if self.head is None:
            print("Catalog is empty. Nothing to delete.")
            return

        removed = self.head.data
        self.head = self.head.next
        print(f"'{removed}' removed from the beginning.")

    # Display
    def display(self):
        if self.head is None:
            print("Catalog is empty.")
            return

        temp = self.head
        print("Library Catalog: ", end="")
        while temp is not None:
            print(f"{temp.data} --> ", end="")
            temp = temp.next
        print("NULL")


def main():
    catalog = LibraryCatalog()

    while True:
        print("\n----- Library Catalog Menu -----")
        print("1. Insert book at beginning")
        print("2. Insert book at end")
        print("3. Delete book from beginning")
        print("4. Display catalog")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            book = input("Enter book title: ")
            catalog.insert_at_beginning(book)

        elif choice == '2':
            book = input("Enter book title: ")
            catalog.insert_at_end(book)

        elif choice == '3':
            catalog.delete_from_beginning()

        elif choice == '4':
            catalog.display()

        elif choice == '5':
            print("Exiting Library Catalog System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()