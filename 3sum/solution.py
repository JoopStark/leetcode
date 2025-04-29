class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        positives, negatives = [], []
        zeros = 0
        result = set()

        for num in nums:
            if num > 0:
                positives.append(num)
            elif num < 0:
                negatives.append(num)
            else:
                zeros += 1
        
        positives_set, negatives_set = set(positives), set(negatives)
        
        if zeros:
            for positive in positives:
                if -positive in negatives_set:
                    result.add((-positive, 0, positive))
            
            if zeros > 2:
                result.add((0, 0, 0))
        
        length = len(positives)
        for i in range(length):
            for j in range(i+1, length):
                target = positives[i] + positives[j]
                if -target in negatives_set:
                    result.add(tuple(sorted([positives[i], positives[j], -target])))

        length = len(negatives)
        for i in range(length):
            for j in range(i+1, length):
                target = negatives[i] + negatives[j]
                if -target in positives_set:
                    result.add(tuple(sorted([negatives[i], negatives[j], -target])))

        return [list(answer) for answer in result]


            

