class Problem13:
    def logic(self,input:list[int])->int:
        newValue:int=0
        for index in range(len(input)):
            if input[newValue] != input[index]:
               newValue += 1
               input[newValue] = input[index]

        return  newValue+1

if __name__ == '__main__':
    instance:Problem13 = Problem13()
    input:list[int] = [0,0,1,1,1,2,2,3,3,4]
    print(instance.logic(input))