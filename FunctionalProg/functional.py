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
                
#Find euclidean distance
    def find_distance(self):
        x = float(input('Enter x value : '))
        y = float(input('Enter y value : '))
        return (x*x + y*y)**0.5

#To find root of quadratic equation
    def solveQuadratic(self):
        coefficient_a = int(input('Enter coefficient of x^2 : '))
        coefficient_b = int(input('Enter coefficient of x : '))
        constant = int(input('Enter constant value : '))
        delta = coefficient_b*coefficient_b - 4 * coefficient_a * constant
        if delta < 0:
            print('Root not possible')
        else :
            root1 = -1*coefficient_b - (delta/(2*coefficient_a))**0.5
            root2 = -1*coefficient_b + (delta/(2*coefficient_a))**0.5
            print('Root 1 : %.2f' %(root1) , 'Root 2 : %.2f' %(root2))    

#wind chill method
    def relative_temperature(self):
        temperature = float(input('Enter Temperature in Fahernheit : '))
        velocity = float(input('Enter wind velocity in miles/hr : '))
        return 35.74 + 0.6215*temperature + ( 0.4275 * temperature - 35.75) * velocity**0.16