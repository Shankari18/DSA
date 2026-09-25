class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps=0
        currentEnd=0
        far=0
        for i in range(len(nums)-1):
            far=max(far,i+nums[i])
            if(i==currentEnd):
                jumps+=1
                currentEnd=far
        return jumps
        