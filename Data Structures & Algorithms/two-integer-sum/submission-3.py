class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap={}

        for i in range(len(nums)):
            need=target-nums[i]
            if need in hashmap:
                return [hashmap[need],i]   # return its index and the current index.

            hashmap[nums[i]]=i