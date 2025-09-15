class Problem23:
    def logic(self,input:list[int])->int:
        answer:int=0
        for value in input:
            answer^=value
        return answer

    def logic_1(self,input:list[int])->int:
        hash_map:dict[int:int] = {}
        for key in input:
            if key in hash_map:
                hash_map[key] = hash_map.get(key)+1
            else:
                hash_map[key] =1

        for key,value in hash_map.items():
            if value ==1 :
                return key
        return 0

if __name__ == '__main__':
    instance:Problem23 = Problem23()
    input:list[int] = [4,1,2,1,2]
    print(instance.logic_1(input))
