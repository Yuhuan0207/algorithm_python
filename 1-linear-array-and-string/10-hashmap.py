class HashMapRelated:
    def strStr(self, haystack, needle):
        #corner case
        if len(needle) > len(haystack):
            return -1

        hash = 7
        needle_length = len(needle)        
        # calculate hash value of needle
        needle_hash = self.hashValueHelper(needle, hash)
        print("needle_hash: " + str(needle_hash))
        
        # iterate haystack and calculate hash value of each sliding window
        cur_hash = self.hashValueHelper(haystack[:needle_length], hash)
        print("cur_hash: " + str(cur_hash))
        if cur_hash == needle_hash:
            return 0
        
        for i in range(needle_length, len(haystack)):
            # calculate new hash value                    
            cur_hash -= ord(haystack[i - needle_length]) * (hash ** (needle_length - 1))
            cur_hash = cur_hash * hash + ord(haystack[i])
            print("cur_hash: " + str(cur_hash))
            # compare and review            
            if cur_hash == needle_hash:
                return i - (needle_length - 1)

        return -1


    def hashValueHelper(self, input_str, hash):
        hash_value = 0
        for i in range(len(input_str)):
            hash_value = hash_value * hash + ord(input_str[i])            
        return hash_value

if __name__ == "__main__":
    test = [
        ("hello", "ll")
    ]

    for haystack, needle in test:        
        print(HashMapRelated().strStr(haystack, needle))    