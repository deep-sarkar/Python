import string
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

#Bubble sort method
    def bubble_sort(self,array):
        length = len(array)
        for i in range(length):
            for j in range(length):
                if array[j] > array[i]:
                    array[i],array[j] = array[j],array[i]

#Merge sort algorithm
    def merge(self,arr, low, mid, high): 
        left_length = mid - low + 1
        right_length = high - mid 
    
        # create temporary arrays 
        left_temp_array = [0 for i in range(left_length)] 
        right_temp_array = [0 for i in range(right_length)] 
    
        #Copy elemnt to left and right temp array 
        for i in range(0 , left_length): 
            left_temp_array[i] = arr[low + i] 
    
        for j in range(0 , right_length): 
            right_temp_array[j] = arr[mid + 1 + j] 
     
        i = 0     # Initial index of first subarray 
        j = 0     # Initial index of second subarray 
        k = low    # Initial index of merged subarray 

        while i < left_length and j < right_length : 
            if left_temp_array[i] < right_temp_array[j]: 
                arr[k] = left_temp_array[i] 
                i += 1
            else: 
                arr[k] = right_temp_array[j] 
                j += 1
            k += 1
    
        while i < left_length: 
            arr[k] = left_temp_array[i] 
            i += 1
            k += 1

        while j < right_length: 
            arr[k] = right_temp_array[j] 
            j += 1
            k += 1
     
    # sub-array of arr to be sorted 
    def mergeSort(self,arr,low,high): 
        if low < high: 
            mid = (low+(high-1))//2
            self.mergeSort(arr, low, mid)       #Sort 1st half
            self.mergeSort(arr, mid+1, high)    #Sort 2nd half
            self.merge(arr, low, mid, high)     #merge

#Prime number
    #Check prime
    def is_prime(self,num):
        n = 2
        while n < num//2 :
            if num % n == 0 :
                return False
            n += 1
        return True
    
    #generate prime in a range
    def prime_in_range(self,low,high):
        count = 0
        for number in range(low,high):
            if self.is_prime(number):
                print(number)
                count += 1
        print('Total : ',count)

#Permutation of string
    def toString(self,array):
        return ''.join(array)
        
    def permute(self,array,low,high):
        if low == high :
            print(self.toString(array))
        else :
            for i in range(low, high + 1):
                array[low],array[i] = array[i],array[low]
                self.permute(array, low + 1, high)
                array[low],array[i] = array[i],array[low]

#Anagran Detection
    def is_anagram(self,string1,string2):
        if type(string1) == str and type(string2) == str :
            str1 = string1.upper()
            str2 = string2.upper()
        list1 = list(str1.replace(' ',''))
        list2 = list(str2.replace(' ',''))
        if len(list1) != len(list2):
            return False
        else :
            self.bubble_sort(list1)
            self.bubble_sort(list2)
            if list1 == list2 :
                return True