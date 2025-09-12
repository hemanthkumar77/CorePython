class Problem17:
    def logic(self,input:list[int])->int:
        voters:int = 1
        majorityElements:int = input[0]
        for i in range(1,len(input)):
            if voters==0:
               voters+=1
               majorityElements=input[i]
            elif majorityElements == input[i]:
                voters+=1
            else:
                voters-=1
        return majorityElements
if __name__ == '__main__':
    instance:Problem17 = Problem17()
    input:list[int] = [2,2,1,1,1,2,2]
    print(f'result:{instance.logic(input)}')