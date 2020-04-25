class StringCalculator:
    def addString(self, num1, num2):
        """
        Add two large numbers in string representation without using operator.

        Parameters:
            num1(str): large number 1
            num2(str): large number 2
        
        Return:
            res(str): addition result.
        
        Psuedocode:
            在共同长度区间:
                sum = num1[i] + num2[i] + carry
                cur = sum % 10
                carry = sum / 10
            在超长区间:
        
        """
        # corner case
        if not num1 or not num2:
            return num1 or num2
        
        carry = 0
        len_iteration = min(len(num1), len(num2))
        res = ""
        #iterate
        for i in range(len_iteration):
            sum = int(num1[-i - 1]) + int(num2[-i - 1]) + carry
            res += str(sum % 10)
            carry = sum // 10
        
        if len(num1) > len_iteration:
            for i in range(len(num1) - len_iteration):                
                sum = int(num1[- len_iteration - 1 - i]) + carry
                res += str(sum % 10)
                carry = sum // 10

        if len(num2) > len_iteration:
            for i in range(len(num2) - len_iteration):
                idx = len(num2) - len_iteration - 1 - i
                sum = int(num2[idx]) + carry
                res += str(sum % 10)
                carry = sum // 10        
        res += str(carry) if carry else ""

        return res[::-1]        

    def addStringQueue(self, num1, num2):
        num1 = list(num1)
        num2 = list(num2)
        carry = 0
        res = [""] * (max(len(num1), len(num2)) + 1)        
        for i in range(len(res) - 1, -1, -1):
            sum = 0
            if num1:
                sum += int(num1.pop())                
            if num2:
                sum += int(num2.pop())            
            sum += carry        
            cur = sum % 10
            carry = sum // 10
            res[i] = str(cur)
        return "".join(res) if res[0] != "0" else "".join(res[1:])




if __name__ == "__main__":
    test = [
        ("123", "1234"),
        ("9", "1")
    ]        
    for num1, num2 in test:
        print(StringCalculator().addStringQueue(num1, num2))