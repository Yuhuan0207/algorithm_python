import time
class DuplicateEvenNum:
    """
    Input array
    """
    def duplicateEvenNum(self, input_arr):
        """
        Duplicate even number in the input_arr. 
        """
        if not input_arr:
            return input_arr
        res = []
        for i in input_arr:
            if i % 2 == 0:
                res.append(i)
            res.append(i)
        return res

    def duplicateEvenNumInPlace(self, input_arr):
        """
        Duplicate even number in the input_arr in place.
        """
        if not input_arr:
            return input_arr        
        right_pointer = len(input_arr) - 1
        for i in range(len(input_arr) -1, -1, -1):
            cur_num = input_arr[i]        
            if cur_num == 0:                        
                continue
            elif cur_num % 2 == 0:
                input_arr[right_pointer] = cur_num
                right_pointer -= 1            
            input_arr[right_pointer] = cur_num
            right_pointer -= 1        
        return input_arr
                
if __name__ == '__main__':
    d = DuplicateEvenNum()
    test_case = []
    test_case.append([])
    test_case.append([1,2,3])
    test_case.append([1,2,3,4,5])    
    for input_arr in test_case:
        print("Input array is: \n" + str(input_arr))
        start_time = time.time()
        print(d.duplicateEvenNum(input_arr))
        print(time.time() - start_time)

    print("------------Inplace-------------")

    test_case_inplace = []
    test_case_inplace.append([])
    test_case_inplace.append([1,2,3,0])
    test_case_inplace.append([1,2,3,4,5,0,0])      
    for input_arr_inplace in test_case_inplace:
        print("Input array is: \n" + str(input_arr_inplace))
        start_time = time.time()
        print(d.duplicateEvenNumInPlace(input_arr_inplace))
        print(time.time() - start_time)