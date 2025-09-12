class Problem19:
    def logic(self,input:list[int],distance:int)->bool:
        hash_map:{int:int} = {}
        for index in range(len(input)):
            if input[index] in hash_map:
               if abs(hash_map[input[index]] - index) <= distance:
                   return True
            hash_map[input[index]] = index
        return False

if __name__ == '__main__':
    input:list[int] = [1,2,3,1,2,3]
    instance:Problem19 = Problem19()
    print(instance.logic(input,2))