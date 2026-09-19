class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        index=0
        n=len(nums)
        for i in range(0,n,1):
            if nums[i]!=val:
                nums[index]=nums[i]
                index+=1
        return index

        