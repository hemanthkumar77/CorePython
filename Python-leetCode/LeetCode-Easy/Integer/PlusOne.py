class Problem2:
    def logic(self,input:list[int])->list[int]:
        for index in range(len(input)-1,-1,-1):
            if input[index] != 9:
                input[index]+=1
                return input
            input[index] = 0
        return [1] + input

if __name__ == '__main__':
    instance:Problem2 = Problem2()
    input:list[int] = [1,3,5,6]
    print(instance.logic(input))
