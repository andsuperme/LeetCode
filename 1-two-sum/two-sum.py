class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        
        for i, num in enumerate(nums): # assigns each value an index
            if target - num in hashmap: # checks for each num the remainder is already in dictionary
                return [i, hashmap[target - num]]
            hashmap[num] = i # adds current number to hashmap