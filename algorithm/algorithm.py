class AlgorithmMethods:

#Binary search method
    def binSearch(self,array,low,high,element):
        if low > high:
            return -1
        mid = (low + high)//2
        if array[mid] > element :
            return self.binSearch(array, low, mid -1, element)
        elif array[mid] == element :
            return mid
        elif array[mid] < element :
            return self.binSearch(array, mid + 1, high , element) 

#Insertion sort method
    def insertion_sort(self,array):
        length = len(array)
        for i in range(1,length):
            temp = array[i]
            j = i-1
            while j >= 0 and array[j] > temp:
                array[j+1] = array[j]
                j -= 1
            array[j+1] = temp