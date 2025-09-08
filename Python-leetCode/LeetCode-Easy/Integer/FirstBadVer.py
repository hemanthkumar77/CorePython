class Problem12:
    def logic(self,n:int)->int:
        first: int = 0
        last: int = n
        result: int = n
        while first <= last:
            mid: int = (first + last) // 2
            'this isBadVersion will be provided by the leet-code'
            if isBadVersion(mid):
                result = mid
                last = mid - 1
            else:
                first = mid + 1
        return result