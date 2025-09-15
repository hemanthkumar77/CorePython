class Problem22:
    def logic(self,input:list[int],count:int)->bool:
        flower_count:int =0
        for index in range(1,len(input)-1,1):
            if input[index-1] == 0 and input[index+1]==0:
               flower_count+=1
        return flower_count==count

if __name__ == '__main__':
    input:list[int] = [1,0,0,0,1]
    instance:Problem22 = Problem22()
    print(instance.logic(input,2))
