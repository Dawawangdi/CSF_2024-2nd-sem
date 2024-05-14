class Solution():
    def productExceptSelf(self, nums):
        '''
        :type nums: List[int]
        :rtype : List[int]
        '''
        res = [1] * len(nums)

        # Calculate prefix products
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        # Calculate postfix products
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
            
        return res
    
sol = Solution()
nums = [1, 2, 3, 4, -5]
print(sol.productExceptSelf(nums))
