class Problem25:
    def logic(self,input:list[int])->list[int]:
        for index in range(0,len(input),2):
            if index>0 and input[index-1] < input[index]:
               self.swap(index-1,index,input)
            if index<len(input)-1 and input[index] > input[index+1]:
                self.swap(index,index+1,input)
        return input

    def swap(self,pos1,pos2,input:list[int])->list[int]:
        temp:int = input[pos1]
        input[pos1] = input[pos2]
        input[pos2] = temp
        return input
if __name__ == '__main__':
    instance2:Problem25 = Problem25()
    input:list[int] = [1,2,3,4,5]
    print(instance2.logic(input))