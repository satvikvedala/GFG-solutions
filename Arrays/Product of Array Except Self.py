class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [0]*len(nums)
        right = [0]*len(nums)
        left[0] = nums[0]
        right[-1] = nums[-1]
        for i in range(1,len(nums)):
            left[i] = left[i-1]*nums[i]
        for i in range(len(nums)-2,-1,-1):
            right[i] = right[i+1]*nums[i]
        for i in range(len(nums)):
            if i == 0:
                nums[i] = right[i+1]
            elif i == len(nums)-1:
                nums[i] = left[i-1]
            else:
                nums[i] = left[i-1]*right[i+1]
        return nums
