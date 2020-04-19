class PartitionArray:
    def movingZero(self, input_arr):
        """
        Move zeros in the input_arr to the end in place. 

        Examples:
            Input: [0,1,0,3,12]
            Output: [1,3,12,0,0]
        Parameters:
            input_arr(List[int]): input array.
        Return:
            None. Edit the array in place.
        """
        # corner case
        if not input_arr:
            return

        # two pointers, 1 scanner, 1 partition boundary
        zero_boundary = 0
        for i in range(len(input_arr)):            
            if input_arr[i] != 0:                
                input_arr[zero_boundary] = input_arr[i]
                zero_boundary += 1        
        while zero_boundary < len(input_arr):
            input_arr[zero_boundary] = 0
            zero_boundary += 1
        return

    def sortColors(self, input_arr):
        """
        Sort them in-place so that objects of the same color are adjacent, with the colors in the order red(0), white(1) and blue(2). (Leetcode 75. Sort Colors)

        Examples:
            Input: [2,0,2,1,1,0]
            Output: [0,0,1,1,2,2]        
        Parameters:
            input_arr(List[int]): input array of colors.
        Return:
            None. Sort in-place.
        """
        # corner case

        # 3 pointers, 1 scanner, 2 partitioning boundary
        i, left_bound, right_bound = 0, 0, len(input_arr) - 1
        while i <= right_bound:
            if input_arr[i] == 0:
                self.swap(input_arr, i, left_bound)
                left_bound += 1
            if input_arr[i] == 2:
                self.swap(input_arr, i, right_bound)
                right_bound -= 1
            if input_arr[i] == 1 or i < left_bound:
                i += 1
        return

    def swap(self, arr, i, j):
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
        return


if __name__ == "__main__":
    test_moving_zero = [
        [0,1,0,3,12],
        [],
        [5,1]
    ]
    # for arr in test_moving_zero:
    #     print("Input array: " + str(arr))
    #     PartitionArray().movingZero(arr)
    #     print("result: " + str(arr))
    #     print("---------------")

    color_arr = [
        [2,0,2,1,1,0],
        [0,0,2,1,0,1]
    ]
    for arr in color_arr:
        print("Input arr: " + str(arr))
        PartitionArray().sortColors(arr)
        print("Output arr: " + str(arr))
        print("--------")
