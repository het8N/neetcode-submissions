class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l1 = []
        l2 = []
        k = k % len(nums)
        for i in range(0,len(nums)-k):
            l1.append(nums[i])
        for j in range(len(nums)-k,len(nums)):
            l2.append(nums[j])
        
        nums[:] = l2 + l1 
        