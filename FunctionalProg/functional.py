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