from utilUnOrderedList import *
u = UnorderedList()   
u.pop()     #Popping while list is empty
u.add(10)  #adding elements in list by default at 1st position
u.add(20)  #adding elements in list by default at 1st position
u.add(85)  #adding elements in list by default at 1st position
u.add(27)  #adding elements in list by default at 1st position
u.add(78)  #adding elements in list by default at 1st position
insert = u.insert(99,3) #adding at specific index
print('insert',insert)
u.remove(85)    #remove element by passing element as argument
u.display()     #Display elements of list
print()
size = u.size()   #checking size of list after every operation
print('size : ',size)
search = u.search(27) #search element
print('search',search)
empty = u.empty()    #checking wether list is empty or not
print('is empty',empty)
index = u.index(100)  #display index of element
print('index of',index)
u.add(903)    #add to 1st position
u.display()
print()
size = u.size()   #checking size of list after every operation
print('size : ',size)
u.append(47)      #adding at last position
u.display()     #Display elements of list
print()
size = u.size()  ##checking size of list after every operation
print('size : ',size)
pop = u.pop()    #popping last element
print('pop',pop)
u.display()     #Display elements of list
print()
size = u.size()   #checking size of list after every operation
print('size : ',size)
delete = u.pop_index(2)
print('pop With argument',delete)  #popping from perticular index
u.display()     #Display elements of list
size = u.size()   #checking size of list after every operation
print('size : ',size)
u.remove(78)
u.display()