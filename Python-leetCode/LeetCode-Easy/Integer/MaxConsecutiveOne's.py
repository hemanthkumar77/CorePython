class Problem24:
    def logic(self,input:list[int])->int:
        counter:int=0
        maxValue:int=-1
        for value in input:
            if value==1:
                counter+=1
                maxValue=max(counter,maxValue)
            else:
                counter=0
        return maxValue
if __name__ == '__main__':
    instance:Problem24 = Problem24()
    input:list[int] = [1,0,1,1,0,1]
    print(instance.logic(input))
