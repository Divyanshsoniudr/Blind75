class Solution:
    def twoSum(self, nums: List[int], target:int) -> List[int]:
        for number in nums:
            firstIndex = nums.index(number)
            compareNums = nums[firstIndex+1 ::]
            if target - number in compareNums:
                secondIndex= nums.index((target-number), firstIndex + 1)
                return [firstIndex, secondIndex]
        return []
