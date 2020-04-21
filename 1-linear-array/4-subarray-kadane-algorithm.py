class KadaneAlgo:
    def MaxSumSubarray(self, input_arr):
        """
        Find the subarray with max subarray.

        Example:
            Input: [-2,1,-3,4,-1,2,1,-5,4],
            Output: 6
            Explanation: [4,-1,2,1] has the largest sum = 6.        

        Parameters:
            input_arr(List[int]): array of integers that might be both positive an negative.

        Return:
            List(int): tuple of result index pair and length of subarray.
        """
        # corner case
        if not input_arr or len(input_arr) == 0:
            return 0

        # iterate the array, save max, cur_max, cur_start, cur_end
        cur_max = max = input_arr[0]
        cur_start = cur_end = start = end = 0
        for i in range(1, len(input_arr)):
            # update current substring
            if cur_max + input_arr[i] < input_arr[i]:
                cur_max = input_arr[i]
                cur_start = i
            else:
                cur_max = cur_max + input_arr[i]
                cur_end = i

            # update global max info
            if max < cur_max:
                max = cur_max
                start = cur_start
                end = cur_end

        return [start, end]


if __name__ == "__main__":
    test = [
        [-2,1,-3,4,-1,2,1,-5,4]
    ]

    for arr in test:
        print(KadaneAlgo().MaxSumSubarray(arr))