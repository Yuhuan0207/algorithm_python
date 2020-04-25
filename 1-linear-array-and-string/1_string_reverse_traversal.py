class ReverseWordsInString:
    def reverseSubstring(self, s, k):
        """
        Reverse the first k characters for every 2k characters 
        counting from the start of the string. (Leetcode 541. Reverse String II)

        Example:
            Input: s = "abcdefg", k = 2
            Output: "bacdfeg"
        Parameters:
            s(str): input string.
            k(int): length of substring.
        Returns:
            res_str(str): reversed string.
        """
        # corner case
        res_str = ""
        section_num = 0
        while (section_num + 1) * k <= len(s):
            cur_str = s[section_num * k : (section_num + 1) * k]
            if section_num % 2 == 0:
                res_str += cur_str[::-1]
            else:
                res_str += cur_str
            section_num += 1
        
        # remaining substring
        rem_str = s[section_num * k:]
        if section_num % 2 != 0:
            res_str += rem_str
        else:
            res_str += rem_str[::-1]
        
        return res_str

    def reverseCharactersInWords(self, s):
        """
        Reverse the order of characters in each word within a sentence while still preserving 
        whitespace and initial word order.. (Leetcode 557. Reverse Words in a String III)

        Example:
            Input: "Let's take LeetCode contest"
            Output: "s'teL ekat edoCteeL tsetnoc"
                
        Parameters:
            s(str): input string
        
        Return:
            res_str(str): output string
        """
        # corner case
        res_str = ""
        start_idx = 0
        while start_idx < len(s):
            if s[start_idx] == ' ':
                res_str += ' '
                start_idx += 1
            else:
                end_idx = s.find(' ', start_idx) if (s.find(' ', start_idx) != -1) else len(s)
                res_str += s[start_idx: end_idx][::-1]
                start_idx = end_idx
        return res_str

    def reverseWordInString(self, s):
        """
        Reverse the word orders in a string. (Leetcode 151. Reverse Words in a String)

        Example:
            Input: "the sky is blue"
            Output: "blue is sky the"

            Input: "  hello world!  "
            Output: "world! hello"
            Explanation: Your reversed string should not contain leading or trailing spaces.

            Input: "a good   example"
            Output: "example good a"
            Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

        Parameters:
            s(str): input sentence as a string.

        Return:
            res_str(str): sentence with reversed word order as input.
        """
        # corner case
        if not s:
            return s
        # Input: "  hello world!  "
        # trim leading/tailing space and reverse the whole string
        
        s = s.strip()[::-1]
        # "hello world!" -> "!dlrow olleh"
        # reverse the word and only append 1 space
        res_str = ""
        start_idx = 0
        while start_idx < len(s):
            if s[start_idx] == " ":
                start_idx += 1
                continue
            end_idx = s.find(" ", start_idx) if s.find(" ", start_idx) != -1 else len(s)
            res_str += s[start_idx:end_idx][::-1]
            res_str += " "
            start_idx = end_idx + 1
        return res_str.strip()


class ReverseWordsInCharArray:
    """
    Reverse array of string - can happen in place. 
    """
    def reverseStringHelper(self, s):
        """
        Reverse the input character array. (Leetcode 344. Reverse String)
        Example:
            s = ["h","e","l","l","o"]
            s = ['o', 'l', 'l', 'e', 'h']

        Parameters:
            s(str): array of characters that needs to be reversed
        
        Returns:
            None. Reverse in place.
        """
        if not s:
            return s
        left = 0
        right = len(s) - 1
        while left < right:
            tmp = s[left]
            s[left] = s[right]
            s[right] = tmp
            left += 1
            right -= 1
        return     


if __name__ == "__main__":
    # 541. Reverse String II
    str_arr = [("abcde", 2), ("abcdef", 3), ("abcdefg", 4)]
    # print(ReverseWordsInString.reverseSubstring.__doc__)
    for s, k in str_arr:
        print("Input string: " + s + "\nk: " + str(k))
        print("Result: " + ReverseWordsInString().reverseSubstring(s, k))

    print("------------------")

    # 557. Reverse Words in a String III
    str_arr2 = ["Let's take LeetCode contest", "Let's take LeetCode contest   "]
    for s in str_arr2:
        print("Input string: " + s)
        print("Result: " + ReverseWordsInString().reverseCharactersInWords(s))

    print("------------------")

    # 151. Reverse Words in a String
    str_arr3 = ["the sky is blue", "  hello world!  ", "a good   example"]
    for s in str_arr3:
        print("Input string: " + s)
        print("Result: " + ReverseWordsInString().reverseWordInString(s))


    print("------------------")
    input_str = "the sky is blue"


    input_arr = ["h","e","l","l","o"]
    ReverseWordsInCharArray().reverseStringHelper(input_arr)
    print(input_arr)
