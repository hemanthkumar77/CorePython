class Problem9:
    def logic(self,input:list[int],limit:int)->int:
        boats:int=0
        left_pointer:int=0
        right_pointer:int=len(input)-1
        'time complexity is n(log n)'
        input.sort()
        while left_pointer<=right_pointer:
            if(input[left_pointer]+input[right_pointer]==limit):
                left_pointer+=1
            right_pointer-=1
            boats+=1
        return boats

if __name__ == '__main__':
    instance:Problem9 = Problem9()
    input:list[int] = [3,2,2,1]
    print(instance.logic(input,3))