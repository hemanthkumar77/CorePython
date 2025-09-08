class Problem3:
    def logic(self,input:list[int])->list[int]:
        mid:int = 0
        start:int =0
        last:int = len(input)-1
        while mid <= last:
            match input[mid]:
                case 0:
                    self.swap_variables(start,mid,input)
                    start+=1
                    mid+=1
                case 1:
                    mid+=1
                case 2:
                    self.swap_variables(mid,last,input)
                    last-=1
        return input

    def swap_variables(self, num_1: int, num_2: int, input: list[int]) -> list[int]:
        temp: int = input[num_1]
        input[num_1] = input[num_2]
        input[num_2] = temp
        return input

if __name__ == '__main__':
    instance:Problem3 = Problem3()
    input:list[int] = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
    print(instance.logic(input))