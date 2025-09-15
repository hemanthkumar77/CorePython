class Problem21:
    def logic(self, num: list[int], num1: list[int]) -> list[int]:
        hash_map1: dict[int:int] = self.store_operation(num)
        hash_map2: dict[int:int] = self.store_operation(num1)
        num.clear()
        for key in hash_map1.keys():
            if key in hash_map1 and key in hash_map2:
                num.append(key)
        return num

    def store_operation(self, num: list[int]) -> dict[int, int]:
        hash_map: dict[int:int] = {}
        for key in num:
            if key in hash_map:
                hash_map[key] = hash_map.get(key) + 1
            else:
                hash_map[key] = 1
        return hash_map

if __name__ == '__main__':
   input:list[int] = [1,2,2,1]
   input1:list[int] = [2,2]
   instance:Problem21 = Problem21()
   print(instance.logic(input,input1))