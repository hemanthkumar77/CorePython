class Problem4:
    def logic(self,input:list[int],k:int)->list[int]:
        self.swap(input,0,len(input)-1)
        self.swap(input,0,k-1)
        self.swap(input,k,len(input)-1)
        return input

    def swap(self,input:list[int],start,end)->list[int]:
        while start<end:
            temp = input[start]
            input[start]=input[end]
            input[end] = temp
            start+=1
            end-=1
        return input

if __name__ == '__main__':
    instance:Problem4 = Problem4()
    input:list[int] = [3,7,8,9,10,11]
    print(instance.logic(input,3))