class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap = {} # its a val : index pair

        for i , n in enumerate(nums):
            difference = target - n
            if difference in prevmap:
                return [prevmap[difference] , i]
            prevmap[n] = i
        return    
        