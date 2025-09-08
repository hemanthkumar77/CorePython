class Problem5:
    def logic(self,input:list[int]):
        left_output =[0]*len(input)
        left_output[0] =1
        for index in range(1,len(input)):
            left_output[index] = left_output[index-1] * input[index-1]

        temp:int=1
        for index in range(len(input)-1,-1,-1):
            left_output[index] = temp * left_output[index]
            temp = temp * input[index]

        print(left_output)

if __name__ == '__main__':
    instance:Problem5 = Problem5()
    input:list[int] = [1,2,3,4]
    instance.logic(input)