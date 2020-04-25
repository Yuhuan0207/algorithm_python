class TraverseBothEnds:
    def sortedSquares(self, input_arr):
        """
        Return the sorted result of numbers in input_arr.
        Parameters:
            input_arr(List[int]): array of non-decreasing integers both positive and negative. 

        Return:
            res_arr(List[int]): array of non-decreasing integers which are square of input_arr.
        """
        left_idx = 0
        right_idx = len(input_arr) - 1
        res_arr = [0] * len(input_arr)
        for i in range(len(input_arr) - 1, -1, -1):
            left = input_arr[left_idx] ** 2
            right = input_arr[right_idx] ** 2
            if left > right:
                res_arr[i] = left
                left_idx += 1
            else:
                res_arr[i] = right
                right_idx -= 1
        return res_arr

    def findUnsortedSubarray(self, input_arr):
        """
        Find the unsorted array that is the only part to be sorted in order to get the whole array sorted.

        Parameters:
            input_arr(List[int]): list of integers.
        Return:
            res(int): length of the subarray that needs to be sorted.
        """
        # corner case
        if not input_arr or len(input_arr) < 2:
            return 0
        # find first dip left -> right: left_idx
        left_idx, right_idx = -1, -1
        for i in range(len(input_arr) - 1):
            if input_arr[i + 1] < input_arr[i]:
                left_idx = i
                break

        # find first peak right -> left: right_idx
        for i in range(len(input_arr) - 1, 0, -1):
            if input_arr[i - 1] > input_arr[i]:
                right_idx = i
                break

        # find min and max between left_idx and right_idx
        if left_idx == right_idx == -1:
            return 0
        cur_min = min(input_arr[left_idx: right_idx + 1])
        cur_max = max(input_arr[left_idx: right_idx + 1])

        # expand the range
        for i in range(0, left_idx):
            if input_arr[i] > cur_min:
                left_idx = i
                break

        for i in range(len(input_arr) - 1, right_idx, -1):
            if input_arr[i] < cur_max:
                right_idx = i
                break
        return 0 if left_idx == right_idx == -1 else (right_idx - left_idx) + 1



if __name__ == "__main__":
    tests = [
        [-4,-1,0,3,10],
        [-7,-3,2,3,11],
        [-1]
    ]
    for arr in tests:
        print(arr)
        print(TraverseBothEnds().sortedSquares(arr))
        print("===========")

    tests2 = [
        [2, 6, 4, 8, 10, 9, 15],
        [1,2,3,4],
        [4,3,2,1]
    ]
    for arr in tests2:
        print(arr)
        print(TraverseBothEnds().findUnsortedSubarray(arr))
        print("----------")        
