class Problem8:
    def logic(self,input:list[int],expected:int)->list[int]:
        left_pointer:int = 0
        right_pointer:int = len(input)-1
        target:bool = False
        while left_pointer < right_pointer:
            sum:int = input[left_pointer] + input[right_pointer]
            if sum == expected:
               target = True
               break
            elif sum<target:
                left_pointer+=1
            else:
                right_pointer-=1
        if target:
            return [left_pointer+1,right_pointer+1]
        else:
            return []

if __name__ == '__main__':
    instance:Problem8 = Problem8()
    input:list[int] = [-1,0]
    print(instance.logic(input,-1))
