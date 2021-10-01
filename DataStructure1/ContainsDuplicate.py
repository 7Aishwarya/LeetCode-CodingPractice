class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hash1 = {}
        for i in range(len(nums)):
            if nums[i] in hash1:
                return True
            hash1[nums[i]] = None
        return False
        