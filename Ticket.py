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