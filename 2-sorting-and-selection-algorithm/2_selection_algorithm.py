from random import randint
class SelectionAlgorithm:
    def findKthSmallest(self, arr, k, start_idx, end_idx):
        """
        Selection algorithm.        

        Parameters:
            arr(List[int]): input array
            k(int): find Kth smallest
            start_idx(int): start index of searching portion
            end_idx(int): end index of search portion

        Returns:
            res(int): value of Kth smallest number in the input array
        """
        random_idx = randint(0, len(arr) - 1)
        pivot_idx = self.partition(arr, random_idx, start_idx, end_idx)
        if pivot_idx == k - 1:
            return arr[pivot_idx]
        elif pivot_idx < k:
            return self.findKthSmallest(arr, k, pivot_idx, end_idx)
        else:
            return self.findKthSmallest(arr, k, start_idx, pivot_idx)

    def partition(self, arr, pivot_idx, start_idx, end_idx):
        """                
        """
        # swap pivot to end of array
        pivot = arr[pivot_idx]
        self.swap(arr, pivot_idx, end_idx)
        
        # partition the whole array
        i = 0
        for j in range(start_idx, end_idx + 1):
            if arr[j] < pivot:
                self.swap(arr, i, j)
                i += 1

        # swap pivot back, return pivot index
        self.swap(arr, i, end_idx)
        return i

    def swap(self, arr, i, j):
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
        return

if __name__ == "__main__":
    test = [
        ([3,2,1,5,6,4], 2),
        ([3,2,3,1,2,4,5,5,6], 4)
    ]
    for arr, k in test:
        print("Array: " + str(arr) + "\nK: " + str(k))
        print(SelectionAlgorithm().findKthSmallest(arr, k, 0, len(arr) - 1))