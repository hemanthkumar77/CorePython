class Problem16:
    def logic(self,haystack:str,needle:str)->int:
        len_haystack,len_needle = len(haystack),len(needle)
        for i in range (len_haystack-len_needle+1):
            if haystack[i:i+len_needle] == needle:
                return i
        return -1

if __name__ == '__main__':
    instance:Problem16 = Problem16()
    print(f'result:{instance.logic("aaaaa","bba")}')