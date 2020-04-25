class SlidingWindow:
    def minSubArrayLen(self, s, nums):
        # corner case
        if not nums or len(nums) == 0:
            return 0
        
        # two pointers sliding window
        left_idx = right_idx = 0
        cur_sum = nums[0]
        valid_flag = False
        min_size = len(nums)
        while right_idx < len(nums) and left_idx < len(nums):            
            if cur_sum >= s:
                # record min_size
                min_size = min(right_idx - left_idx + 1, min_size)
                
                # move left pointer
                cur_sum -= nums[left_idx]
                left_idx += 1               
                
                # turn on valid flag
                valid_flag = True
            else:
                # move right pointer
                right_idx += 1
                cur_sum += nums[right_idx] if right_idx < len(nums) else 0
        
        return min_size if valid_flag else 0

if __name__ == "__main__":
    test = [
        (7, [2,3,1,2,4,3])
    ]
    for s, arr in test:
        print(SlidingWindow().minSubArrayLen(s, arr))