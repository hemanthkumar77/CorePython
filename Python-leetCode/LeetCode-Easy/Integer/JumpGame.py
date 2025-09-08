class Problem6:
     def logic(self,input:list[int])->bool:
         last_index:int = input[len(input)-1]
         for index in range(len(input)-2,-1,-1):
             if index+input[index] >=last_index:
                 last_index =index
         return last_index==0

if __name__ == '__main__':
    instance:Problem6 = Problem6()
    input:list[int] = [3,2,1,0,4]
    print(instance.logic(input))