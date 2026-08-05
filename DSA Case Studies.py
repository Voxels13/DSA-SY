#Explicit > Implicit

#To run the programs, delete the multi line strings encasing the lines of code you want to run

#Case Study 1

#7 Parking Garage 

'''
Conditions:

Maximum Parking capacity is 10 vehicles
Only Car and Bike are allowed
Vehicle Registration number must be unique
Trucks and buses are not permitted


Operations:

Park Vehicle(Push)
Exit Vehicle(Pop)
Top Vehicle(Peek)
Display Parked Vehicles
'''


#---------------------
'''
def is_full_check(stack,n):
    return len(stack) >= n

def is_empty_check(stack):
    return len(stack) == 0

def park_vehicle(choice,stack,n,reg_no):

    if not is_full_check(stack,n):
        stack_info = (f"Car : {reg_no}" if choice == 1 else f"Bike : {reg_no}")
        stack.append(stack_info) 
        print(f"Car has been parked" if choice == 1 else "Bike has been parked\n")
    else:
        print("Garage is full at the moment :[\n")

def exit_vehicle(stack,parked_list):

    if not is_empty_check(stack):
        exitted_vehicle = stack.pop()
        reg_no = exitted_vehicle.split(":")[-1].strip()
        if reg_no in parked_list:
            parked_list.remove(reg_no)

        print(f"{exitted_vehicle} has checked out of the garage\n")
        print(f"Space remaining: {len(stack)}")

    else:
        print("The Garage is currently empty\n")

def top_vehicle(stack):
    if not is_empty_check(stack):
        print(f"At the tail end: {stack[-1]}\n")
    else:
        print("Garage is empty\n")
    
def permit(choice,stack,n,reg_no):
    if choice == 1 or choice == 2:
        park_vehicle(choice,stack,n,reg_no)
    else:
        print("You cannot park such Vehicles here\n")

def display(stack):
    if not is_empty_check(stack):
        print(stack)
    else:
        print("Stack is Empty")

#---------------------

def main():
    n = 10 #Max vehicle
    stack = []
    parked_vehicles = []
    is_running = True

    while is_running:
        print("\nState Vehicle Type:\n1.Car\n2.Bike\n3.Other")
        try:
            choice = int(input(":"))
        except ValueError:
            print("Please enter a valid integer input\n")


        print("Do you want to\n1.Park\n2.Take Out last vehicle\n3.See Vehicle at End\n4.Display Garage\n5.Quit")
        op = int(input("(1/2/3/4):"))

        if op == 1:
             #Check for Unique Regist Numbers.
            regis_no = input("Enter registration number: ")
            if regis_no not in parked_vehicles:
                parked_vehicles.append(regis_no)
                print("Vehicle has been registered successfully\n")
                permit(choice, stack, n, regis_no)
            else:
                print("Vehicle already registered\n")


        elif op == 2:
            exit_vehicle(stack,parked_vehicles)

        elif op == 3:
            top_vehicle(stack)

        elif op == 4:
            display(stack)

        elif op == 5:
            print("Exiting Program...")

            is_running = False
        else:
            print("Please enter a valid option!")

main()
'''

#8 Call Stack in Programming

'''
Conditions:
• Maximum call stack depth is 15.
• Function names must start with a letter.
• Recursive calls are allowed only up to 3 consecutive levels.
• Reject invalid function names.

Operations:
• Call Function (Push)
• Return from Function (Pop)
• Current Function (Peek)
'''


'''

#-------------------------------
def func1():
    print ("This is function1\n")

def func2():
    print ("This is function2\n")

def recur(level):
    print (f"This is level {level}")

    print()

    if level >= 3:
        print(f"Reached Max Level {level}! | Recursion stopped\n")
        return

    recur(level+1)

    print(f"Exiting Level {level}")

    print()

def is_full(stack,n):
    return len(stack) >= n

def is_empty(stack):
    return len(stack) == 0


def call_function(stack,n,func_name):
    if not is_full(stack,n):
        stack.append(func_name)
        print(f"Function {func_name} has been added to the stack!\n")
    else:
        print("Function Load is full at the moment\n")

def return_function(stack):
    if not is_empty(stack):
        popped_func = stack[-1] #This will give a string btw , cause we entered a string into the thingy
        if popped_func == 'func1':
            func1()
        elif popped_func == 'func2':
            func2()
        elif popped_func == 'recur':
            recur(0)
        stack.remove(popped_func)
    else:
        print("The stack is empty!\n")

def current_function(stack):
    if not is_empty(stack):
        top = stack[-1]
        print(f"Current Function to be executed: {top}\n")
    else:
        print("Stack is empty\n")

def display(stack):
    print(f"Current Function Stack\n{stack}\n")


#------------------------------

def main():
    n = 15 #Stack Depth
    func_names = ['func1','func2','recur']
    stack = []
    is_running = True

    while is_running:
        print("Operations:\n1.Call Function\n2.Return from Function\n3.Check Current Function\n4.Display Stack\n5.Quit")
        op = int(input(":"))

        if op == 1:
            print(f"Available Functions\n{func_names}")
            func_name = input("Enter a function: ").lower()
            if func_name in func_names:
                call_function(stack,n,func_name)
            else:
                print("Said function does not exist")

        elif op == 2:
            return_function(stack)

        elif op == 3:
            current_function(stack)

        elif op == 4:
            display(stack)

        elif op == 5:
            print("Exiting Program...")
            is_running = False

        else:
            print("Please enter a valid option!")
main()
'''


#Case Studies 2

#1 Railway Ticket Counter Queue

'''
Conditions:

-The queue can hold a maximum of 50 passengers.
-Duplicate Ticket IDs are not allowed.
-Only confirmed passengers can join the queue.
-If the queue is full, no new passenger can enter.

Operations:

-Add Passenger (Enqueue)
-Serve Passenger (Dequeue)
-View First Passenger (Front)
-Display Passenger Queue

'''


'''
#-----------------------------------------

def is_full(queue,n):
    return len(queue) >= n

def is_empty(queue):
    return len(queue) == 0

def add_passanger(queue,n,ticket_no):

    if not is_full(queue,n):
        queue.append(ticket_no)
        print("Passanger has been added to the Queue!\n")
    else:
        print("Passanger Queue is Full!\n")

def board_passanger(queue,boarded_ticket):

    if not is_empty(queue):
        boarded = queue.pop(0)
        boarded_ticket.remove(boarded)
        print(f"Passanger having Ticket: <{boarded}> has been boarded onto the train\n")
    else:
        print("The Passanger queue is empty! There is no passanger to board\n")

def firstpassanger(queue):

    if not is_empty(queue):
        top = queue[0]
        print(f"Ticket of first passanger to be boarded: {top}")
    else:
        print("The Queue is currently Empty!")

def passanger_list(queue):

    if not is_empty(queue):
        print(f"Passanger Queue:\n{queue}")
    else:
        print("The Queue is currently Empty!")

#-----------------------------------------

def main():
    n = 50
    queue = []
    tickets = []
    is_running = True

    while is_running:
        print("-------------RAILWAY STATION-------------")
        print("1.Buy Ticket\n2.Board Passanger into the Train\n3.Front of Queue\n4.Display Passengers Queue\n5.Quit")
        try:
            op = int(input(":"))
        except ValueError:
            print("Please enter a valid option!\n")

        if op == 1:
            ticket_no = input("Enter ticket number: ")   #String input
            if ticket_no not in tickets:
                tickets.append(ticket_no)
                print(f"Ticket <{ticket_no}> has been assigned!\n")
                add_passanger(queue,n,ticket_no)
            else:
                print(f"Ticket already assigned! Please assign a new distinct ticket!\nAllotted Tickets = {tickets}\n")


        elif op == 2:
            board_passanger(queue,tickets)

        elif op == 3:
            firstpassanger(queue)

        elif op == 4:
            passanger_list(queue)

        elif op == 5:
            print("Exiting..")
            is_running = False

        else:
            print("Please enter a valid option!")

#-----------------------------------------------

main()

'''

#3 is too similar to the one above so i just skipped it.


#Case Studies 3

#3 Library Book ID's

'''
Tasks:
Create a linked list containing:
 B101, B102, B103

Insert B104.

Insert B105.

Display the final linked list.
'''

'''
#----------------------
class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

def createLL(dataset, head):

    if head.data is None:
        print("Linked List is empty")

    temp = head
    i = 1
    while i < len(dataset):
        temp.next = Node(dataset[i])
        temp = temp.next
        i+=1

def insertnewnode(nodeval,position,head):  #NOTE make one where it can take in a list and then adds the elements of the list onto the Linked List

    newnode = Node(nodeval)

    if position == 0:
        newnode.next = head

        return head

    current = head
    prev = None

    for i in range (1,position+1):
        prev = current
        current = current.next

    prev.next = newnode
    newnode.next = current

    return head

def displayLL(head):

    temp = head
    while temp is not None:
        print(f"{temp.data}-->",end='')
        temp = temp.next
    print("Null")



def main():
    dataset = ['B101','B102','B103']

    LLhead = Node(dataset[0])

    #Create Initial Linked List

    createLL(dataset,LLhead)

    #Display the Linked List

    displayLL(LLhead)

    #Insert a value into the linked list (takes in value and position)

    newval = input("Enter new node to add:")
    pos = int(input("Enter position (where to add) : "))

    newhead = insertnewnode (newval,pos,LLhead)

    newval = input("Enter new node to add:")
    pos = int(input("Enter position (where to add) : "))
    
    newhead = insertnewnode (newval,pos,LLhead)

    #Display new LL

    displayLL(newhead)


main()
'''



#Case Study 16 : University Course Registration

'''
Tasks:

Display the courses.

Delete Java.

Insert Cloud Computing.

Display the updated course list.

'''

'''
class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

def createLL(dataset):

    head = Node(dataset[0])

    temp = head

    i = 1

    while i < len(dataset):
        temp.next = Node(dataset[i])
        temp = temp.next
        i+=1

    return head

def insertnode(nodeval, position, head):

    temp = head
    prev = None

    newnode = Node(nodeval)

    if position == 0:
        newnode.next = head
        return head

    for i in range(1,position+1):
        prev = temp
        temp = temp.next

    prev.next = newnode
    newnode.next = temp

    return head

def deletenode(nodeval, head):

    temp = head
    prev = None

    if nodeval == head.data:
        newhead = head.next
        return head

    while temp is not None:
        if temp.data == nodeval:
            prev.next = temp.next
            return head

        prev = temp
        temp = temp.next

    print("No such values exist")
    return head
    

def displayLL(head):

    temp = head

    while temp is not None:
        print(f"{temp.data}-->",end='')
        temp = temp.next
    print("Null")


def main():

    InitialCouseSet = ['Python','Java','C++','AI']

    #Create Linked List of initial courses

    LLhead = createLL(InitialCouseSet)
    #Display the initial LL

    print("Course List:")
    displayLL(LLhead)

    #Delete 'Java'

    newLLhead = deletenode('Java',LLhead)

    print()
    print("Delted 'Java' from Course list\n")
    displayLL(newLLhead)

    #Insert 'Cloud Computing' (Here, lets place it at the end of the LL)

    NewLLhead = insertnode('Cloud Computing',3,newLLhead)
    print()
    print("Added Cloud Computing to Course List\n")

    print("New Course List:")
    displayLL(NewLLhead)

main()

'''
