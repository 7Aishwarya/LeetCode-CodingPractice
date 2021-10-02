class Solution(object):
    def search(self, nums, target, l_index, r_index):
        if r_index >= l_index:
            mid_index = (l_index + r_index)//2
            if target == nums[mid_index]:
                return mid_index
            elif target > nums[mid_index]:
                return self.search(nums, target, mid_index + 1, r_index)
            elif target < nums[mid_index]:
                return self.search(nums, target, l_index, mid_index - 1)
        return l_index
                
        
        
            
            
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l_index = 0
        r_index = len(nums) - 1
        ans = self.search(nums, target, l_index, r_index)
        return ans
        
        
        