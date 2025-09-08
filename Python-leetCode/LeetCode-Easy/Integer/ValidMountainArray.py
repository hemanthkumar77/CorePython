class Problem7:
    def logic(self,input:list[int])->bool:
        first_Peek =None
        'find the peek element'
        for ind in range(1,len(input)-1):
            if (input[ind]>input[ind-1] and input[ind]>input[ind+1]):
                first_Peek= ind
                break
        'check if peek is present'
        if first_Peek==None:
            return False
        'check the left side is ascending'
        for index in range(0,first_Peek):
            if not input[index+1] > input[index]:
                return False
        'check the right side is descending'
        for index in range(first_Peek,len(input)-1):
            if not input[index] > input[index+1]:
                return False
        return True

if __name__ == '__main__':
    instance:Problem7 = Problem7()
    input:list[int] = [0,3,2,1]
    print(instance.logic(input))
