class BinarySearch:
    def binarySearch(self, arr, target):
        if not arr or len(arr) == 0:
            return -1
        
        left = 0
        right = len(arr)
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                right = mid
            else:
                left = mid + 1
        return -1

    def binarySearchFirst(self, arr, target):
        left, right = 0, len(arr)
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left if (left < len(arr) and arr[left] == target) else -1        

    def binarySearchLast(self, arr, target):
        left, right = 0, len(arr)
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return right - 1 if arr[right - 1] == target else -1

    def binarySearchInsertionPosition(self, arr, target):
        """
        Find the target insertion position in arr.
        (First occurrence index or index of first number larger than target)
        """
        left = 0
        right = len(arr)
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left

    def binarySearchRotatedArray(self, arr):
        left, right = 0, len(arr) - 1
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] > arr[right]:
                left = mid + 1
            else:
                right = mid
        return arr[left]
    
    def binarySearchUnknownSize(self, arr, target):       
        # 1. find right index, keep left index at the same time
        if reader.get(0) == target:
            return 0
        
        left, right = 0, 1
        while reader.get(right) < target:
            left = right
            right *= 2
        
        return self.binarySearch(reader, left, right + 1, target)
    
    def binarySearchHelper(self, reader, left, right, target):        
        while left < right:
            mid = left + (right - left) // 2
            num = reader.get(mid)
            if num == target:
                return mid
            elif num > target:
                right = mid
            else:
                left = mid + 1
        return left if reader.get(left) == target else -1
        
class Reader:
    def __init__(self):
        pass

    def get(self, index):
        pass



if __name__ == "__main__":
    test = [
        ([-1,0,3,5,9,12], 9),
        ( [-1,0,3,5,9,12], -2)        
    ]
    print("Regular binary search:")
    for arr, target in test:
        print("Array: " + str(arr) + "\nTarget: " + str(target))
        print(BinarySearch().binarySearch(arr, target))

    test_duplicate = [
        ([-1,0,3,5,9,9,12], 9),
        ([-1,0,3,5,9,9,12], -2),
        ([1],1),
        ([1,1],2)
    ]    
    for arr, target in test_duplicate:        
        print("Array: " + str(arr) + "\nTarget: " + str(target))
        print("First occurrence of " + str(target) + " is index: " + str(BinarySearch().binarySearchFirst(arr, target)))
        print("Last occurrence of " + str(target) + " is index: " + str(BinarySearch().binarySearchLast(arr, target)))

    test_rotated = [
        [4,5,6,7,0,1,2],
        [3,4,5,1,2] 
    ]
    for arr in test_rotated:
        print("Array: " + str(arr))
        print("Min number is: " + str(BinarySearch().binarySearchRotatedArray(arr)))