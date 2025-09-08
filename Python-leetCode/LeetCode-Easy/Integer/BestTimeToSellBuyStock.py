class Problem10:
    def logic(self,input:list[int]):
        min_cost =float('inf')
        max_profit=0
        for price in input:
            if price < min_cost:
                min_cost = price
            profit:int = price - min_cost
            if profit > max_profit:
               max_profit = profit
        return max_profit

if __name__ == '__main__':
    instance:Problem10 = Problem10()
    input:list[int] = [1, 3, 6, 9, 11]
    print(instance.logic(input))

