# When given a list of numbers and a target number, 
# this code will output the first two numbers which add up to the target number.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solutions = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    solutions.append(i)
                    solutions.append(j)
        return (solutions[0],solutions[1])
