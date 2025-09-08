class Problem11:
    def logic(self,input:list[int],target:int):
        hashmap:dict[int:int] = {}
        for value,key in enumerate(input):
            current_val:int = target-key
            if current_val in hashmap:
                return [hashmap.get(current_val),value]
            hashmap[key]=value
        return []

if __name__ == '__main__':
    instance:Problem11 = Problem11()
    input:list[int] = [3,3]
    print(instance.logic(input,6))
