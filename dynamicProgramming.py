#Jump Game I (leetcode)
    def canJump(self, nums: List[int]) -> bool:
        maxrange = 0
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False
        for i in range(len(nums)-1):
            if nums[i]!=0:
                maxrange = max(maxrange,i+nums[i])
                if maxrange >= len(nums)-1:
                    return True
            else:
                if maxrange<=nums[i]+i:
                    break
                else:
                    continue
        return False
