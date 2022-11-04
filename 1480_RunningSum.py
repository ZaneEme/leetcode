class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        runSum = 0
        for i in range(len(nums)):
            runSum += nums[i]
            nums[i] = runSum
        return nums
    
if __name__=="__main__":
    S = Solution()
    print(S.runningSum([1,2,3,4]))
    print(S.runningSum([1,1,1,1,1]))
    print(S.runningSum([3,1,2,10,1]))