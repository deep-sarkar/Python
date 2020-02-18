from utilOrderedList import OrderedList
class OrderedListTest:
    o = OrderedList()
    number_of_elements = int(input('Enter number of elements : '))
    for i in range(number_of_elements):
        element = input('enter element : ')
        o.add(element)
    
    o.display()
    print()
    while True:
        print('''\n1.add 2.display 3.size 4.search 5.index of element 6.is empty 7.pop 8.pop index 9.remove ''')
        operation = int(input('Enter operation : '))
        if operation == 1 :
            element = input('add element : ')
            o.add(element)
        elif operation == 2 :
            o.display()
        elif operation == 3 :
            size = o.size()
            print('size : ',size)
        elif operation == 4 :
            element = input('Enter element : ')
            search = o.search(element)
            print('Search : ',search)
        elif operation == 5 :
            element = input('Enter element : ')
            index = o.index(element)
            print('Index : ',index)
        elif operation == 6 :
            empty = o.empty()
            print('Empty : ',empty)
        elif operation == 7 :
            pop = o.pop()
            print('pop : ',pop)
        elif operation == 8 :
            element = int(input('Enter element : '))
            pop_index = o.pop_index(element)
            print('Pop index : ',pop_index)
        elif operation == 9 :
            element = input('Enter element : ')
            o.remove(element)
        else:
            break

       