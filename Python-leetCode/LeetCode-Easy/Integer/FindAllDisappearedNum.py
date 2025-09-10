class Problem15:
    def logic(self,input:list[int])->list[int]:
        'here we need to map the value array will have the value 1 to n and index is 0 to n-1'
        'step 1: map the array value(1 to n) to array index (0,n-1)'
        'step 2: then multiple to -1 to update value in array (duplicates indexed position values will be positive)'
        for _,value in enumerate(input):
            index = abs(value)-1
            input[index] = -1*abs(input[index])
        result:list[int] = []
        for index,value in enumerate(input):
            'step 3: the value which is positive that index+1 is the missing value in the array'
            if value >0:
                result.append(index+1)
        return result
if __name__ == '__main__':
    instance:Problem15 = Problem15()
    input:list[int] = [1,4,3,4,1]
    print(instance.logic(input))
