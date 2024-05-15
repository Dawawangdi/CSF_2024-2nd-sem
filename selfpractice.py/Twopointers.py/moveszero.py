class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #This code implements an algorithm to move all zeros in a list of integers (nums) to the end 
        #while maintaining the relative order of non-zero elements
        l = 0  
        #l = 0: Initializes a variable l to 0. This will be used as the left pointer 
        for r in range(len(nums)):
            #r right pointer, iterates over len of num list.
            if nums[r] is not 0:
                #if nums[r]:: Checks if the current element at index r is non-zero
                nums[l], nums[r] = nums[r], nums[l]
                l+=1

        return nums
    
sol = Solution ()
nums = [3,4,0,7,8,0,6,78,900,76,00]
print(sol.moveZeroes(nums))




           