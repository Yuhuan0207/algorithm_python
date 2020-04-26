import math
class SortingAlgorithm:
    def bubbleSort(self, arr):
        """
        Bubble sort. 
        Sort two numbers in the bubble in every iteration. 
        """
        sorted = False
        while not sorted:
            sorted = True
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    self.swap(arr, i, i + 1)
                    sorted = False
        return

    def selectionSort(self, arr):
        """
        Selection sort.
        Select the min in unsorted part and put in sorted part.
        """
        sorted_boundary = 0
        while sorted_boundary < len(arr):
            cur_min = arr[sorted_boundary]
            min_idx = sorted_boundary
            for i in range(sorted_boundary, len(arr)):
                if arr[i] < cur_min:
                    cur_min = arr[i]
                    min_idx = i            
            self.swap(arr, sorted_boundary, min_idx)
            sorted_boundary += 1

        return

    def insertionSort(self, arr):
        """
        Insertion sort.
        Pick the first unsorted element, insert to the right place in sorted part.
        """
        for unsorted_idx in range(1, len(arr)):
            cur_idx = unsorted_idx
            while cur_idx > 0 and arr[cur_idx] < arr[cur_idx - 1]:
                self.swap(arr, cur_idx, cur_idx - 1)
                cur_idx -= 1
        return 

    def mergeSort(self, arr, start, end):
        """
        Merge sort algorithm. - Divide and Conquer
        """    
        if not arr or start >= end:
            return
        middle = (start + end) // 2        
        self.mergeSort(arr, start, middle)
        self.mergeSort(arr, middle + 1, end)
        self.merge2(arr, start, middle, end)
        # print("Array: " + str(arr))
        return

    def merge(self, arr, start, middle, end):

        tmp = [0] * (end - start + 1)
        left_idx = start
        right_idx = middle + 1
        i = 0
        while left_idx <= middle and right_idx <= end:
            left = arr[left_idx]
            right = arr[right_idx]
            if left <= right:
                tmp[i] = left
                left_idx += 1
            else:
                tmp[i] = right
                right_idx += 1
            i += 1
        while left_idx <= middle:
            tmp[i] = arr[left_idx]
            i += 1
            left_idx += 1
        while right_idx <= end:
            tmp[i] = arr[right_idx]
            i += 1
            right_idx += 1
        arr[start: end + 1] = tmp
        return

    def merge2(self, arr, start, middle, end):
        """
        Merge helper function for merge sort algorithm.
        """
        tmp_arr = [0] * (end - start + 1)
        left_idx = start
        right_idx = middle + 1

        for i in range(0, end + 1 - start):
            left = arr[left_idx] if left_idx <= middle else math.inf
            right = arr[right_idx] if right_idx <= end else math.inf
            if left < right:
                tmp_arr[i] = left
                left_idx += 1
            else:
                tmp_arr[i] = right
                right_idx += 1
        # print("tmp_arr: " + str(tmp_arr) + "\n---------")
        arr[start:end + 1] = tmp_arr
        return

    def quickSort(self, arr, start_idx, end_idx):
        """
        Implementation of quick sort algorithm.
        
        Step breakdown:
            1.pick pivot_index, put pivot to end_index
            2.while iterating the whole array:
                keep a boundary - keep elements < pivot on the left of this boundary
            3.swap(arr, boundary, end_index) -> bring pivot to right position
            quickSort(start, pivot_idx - 1)
            quickSort(pivot_idx + 1, end)
        """
        if not arr or start_idx >= end_idx:
            return
        
        pivot_idx = self.findPivotIndex(start_idx, end_idx)
        pivot = arr[pivot_idx]
        self.swap(arr, pivot_idx, end_idx)
        partition_idx = start_idx
        for i in range(start_idx, end_idx):
            if arr[i] <= pivot:
                self.swap(arr, i, partition_idx)
                partition_idx += 1
        self.swap(arr, partition_idx, end_idx)
        self.quickSort(arr, start_idx, partition_idx - 1)
        self.quickSort(arr, partition_idx + 1, end_idx)
        return

    def findPivotIndex(self, start, end):
        return (start + end) // 2

    def radixSort(self, arr):
        pass

    def bucketSort(self, arr):
        """
        Implementation of bucket sort algorithm.
        """
        max_value = max(arr)
        bucket_arr = [-1] * (max_value + 1)
        for num in arr:
            bucket_arr[num] = num
        res = []        
        for num in bucket_arr:
            if num != -1:
                res.append(num)        
        return res




    def swap(self, arr, i, j):
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp        
        return


if __name__ == "__main__":
    tests = [
        [7,5,2,6,3]
    ]

    for arr in tests:
        print("Input array: " + str(arr))
        arr1 = arr[:]
        SortingAlgorithm().bubbleSort(arr1)
        print("Bubble sort: " + str(arr1))
        arr2 = arr[:]        
        SortingAlgorithm().selectionSort(arr2)
        print("Selection sort: " + str(arr2))
        arr3 = arr[:]        
        SortingAlgorithm().insertionSort(arr3)
        print("Insertion sort: " + str(arr3))
        arr4 = arr[:]
        SortingAlgorithm().mergeSort(arr4, 0, len(arr4) - 1)
        print("Merge sort: " + str(arr4))
        arr5 = arr[:]
        SortingAlgorithm().quickSort(arr5, 0, len(arr5) - 1)
        print("Quick sort: " + str(arr5))
        # arr6 = arr[:]
        # SortingAlgorithm().radixSort(arr6)
        # print("Radix sort: " + str(arr6))
        arr7 = arr[:]        
        print("Bucket sort: " + str(SortingAlgorithm().bucketSort(arr7)))
        print("-------")