class Problem18:
    def logic(self,input:list[int],maxCandies:int)->list[bool]:
        max_candy:int = max(input)
        values:list[bool] = [False] * (len(input))
        for index,candy in enumerate(input):
            if (candy+maxCandies >= max_candy):
                values[index] = True
        return values

if __name__ == '__main__':
     input:list[int]=[4,2,1,1,2]
     instance:Problem18 = Problem18()
     print(instance.logic(input,1))
