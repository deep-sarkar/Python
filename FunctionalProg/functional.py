class Functional:

#Read and print 2d array method
    def read_array(self):
        row = int(input('Enter number of rows : '))
        column = int(input('number of columns : '))
        array = [[0 for column_index in range(column)] for row_index in range(row)]
        for row_index in range(row):
            for column_index in range(column):
                array[row_index][column_index] = int(input('Enter element : '))
        for row_index in array:
            print(row_index)
        return array

#Sum of 3 digit in array equal to zero
    def sumOfThree(self):
        num_of_ele = int(input('Enter number of elements : '))
        array = [0 for index in range(num_of_ele)]
        for index in range(num_of_ele):
            array[index] = int(input('Enter element : '))
        print(array)
        for i in range(num_of_ele):
            j = i+1
            for j in range(j,num_of_ele):
                k = j+1
                for k in range(k,num_of_ele):
                    if array[i] + array[j] + array[k] == 0 :
                        print(array[i] , array[j], array[k])
                
