class AlgorithmMethods:

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
  