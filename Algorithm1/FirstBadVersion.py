# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left<=right:
            mid = (left+right)//2
            return_value = isBadVersion(mid)
            if return_value == True and not isBadVersion(mid-1):
                return mid
            elif return_value == True and isBadVersion(mid-1):
                right = mid
            else:
                left = mid + 1
        return left
            
                