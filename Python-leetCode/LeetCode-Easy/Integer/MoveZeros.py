class Problem20:
    def logic(self,input:list[int])->list[int]:
        zero_index:int=0
        for index in range (len(input)):
            if input[index] != 0:
               temp:int = input[index]
               input[index] = input[zero_index]
               input[zero_index] = temp
               zero_index+=1
        return input
if __name__ == '__main__':
    instance:Problem20 = Problem20()
    input:list[int] = [0,1,0,3,12]
    print(instance.logic(input))
