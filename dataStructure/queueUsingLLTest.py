from queueUsingLL import *
class QueueLLTest:
    q = QueueUsingLinkedList()
    n = int(input('Enter number of elements : '))
    for i in range(n):
        element = input('Add element to queue : ')
        q.enque(element)
    q.display()
    print()
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    q.display()