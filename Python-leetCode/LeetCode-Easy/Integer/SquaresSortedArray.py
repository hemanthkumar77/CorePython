class Problem1:
    def logic(self,input:list[int])->list[int]:
        result = []
        left_pointer:int =0
        right_pointer:int= len(input)-1
        temp:int
        while left_pointer <= right_pointer:
            if abs(input[left_pointer]) > abs(input[right_pointer]):
                temp = input[left_pointer]
                left_pointer+=1
            else:
                temp = input[right_pointer]
                right_pointer-=1
            result.append(temp*temp)
        # it will completely reverse all the values in list and then it will return
        return result[::-1]

if __name__ == '__main__':
    instance:Problem1 = Problem1()
    input:list[int] = [-4,-1,0,3,10]
    print(instance.logic(input))