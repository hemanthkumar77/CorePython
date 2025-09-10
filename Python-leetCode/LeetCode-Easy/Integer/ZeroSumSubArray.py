class Problem14:
    def logic(self, input: list[int]) -> bool:
        hash_map: dict[int:int] = {}
        cur_sum: int = 0
        hash_map[0]=-1
        for index in range(len(input)):
            cur_sum += input[index]
            if cur_sum in hash_map:
                return True
            hash_map[cur_sum] = index
        return False


if __name__ == '__main__':
    instance: Problem14 = Problem14()
    input: list[int] = [100, -50, -50, 200, -100, -100]
    print(instance.logic(input))
