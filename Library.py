def is_full_check(stack,n):
    return len(stack) >= n

def is_empty_check(stack):
    return len(stack) == 0

def return_book(choice,stack,n,book_id):

    if not is_full_check(stack,n):
        stack_info = (f"Fiction : {book_id}" if choice == 1 else f"Non-Fiction : {book_id}")
        stack.append(stack_info)
        print("Fiction book has been returned\n" if choice == 1 else "Non-Fiction book has been returned\n")
        return True
    else:
        print("Return bin is full at the moment :[\n")
        return False

def process_book(stack,returned_list):

    if not is_empty_check(stack):
        processed_book = stack.pop()
        book_id = processed_book.split(":")[-1].strip()
        if book_id in returned_list:
            returned_list.remove(book_id)

        print(f"{processed_book} has been shelved back\n")
        print(f"Space used in bin: {len(stack)}\n")

    else:
        print("The Return Bin is currently empty\n")

def top_book(stack):
    if not is_empty_check(stack):
        print(f"Last returned: {stack[-1]}\n")
    else:
        print("Return Bin is empty\n")

def permit(choice,stack,n,book_id):
    if choice == 1 or choice == 2:
        return return_book(choice,stack,n,book_id)
    else:
        print("This category cannot be accepted here\n")
        return False

def display(stack):
    if not is_empty_check(stack):
        print("Return Bin (top -> bottom):")
        for book in reversed(stack):
            print(f"  {book}")
        print()
    else:
        print("Return Bin is empty\n")

#---------------------

def main():
    n = 100 #Max books in return bin
    stack = []
    returned_books = []
    is_running = True

    while is_running:
        print("\nDo you want to\n1.Return Book\n2.Shelve Last Returned Book\n3.See Last Returned Book\n4.Display Return Bin\n5.Quit")
        try:
            op = int(input("(1/2/3/4/5):"))
        except ValueError:
            print("Please enter a valid integer input\n")
            continue

        if op == 1:
            print("State Book Category:\n1.Fiction\n2.Non-Fiction\n3.Other")
            try:
                choice = int(input(":"))
            except ValueError:
                print("Please enter a valid integer input\n")
                continue

            book_id = input("Enter book ID: ")
            if book_id not in returned_books:
                if permit(choice, stack, n, book_id):
                    returned_books.append(book_id)
                    print("Book has been registered successfully\n")
            else:
                print("Book already registered\n")

        elif op == 2:
            process_book(stack,returned_books)

        elif op == 3:
            top_book(stack)

        elif op == 4:
            display(stack)

        elif op == 5:
            print("Exiting Program...")
            is_running = False
        else:
            print("Please enter a valid option!")

main()
