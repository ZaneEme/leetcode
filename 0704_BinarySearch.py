class Solution:
    def search(self, nums: list[int], target: int) -> int:
        leftSide = 0
        rightSide = len(nums) - 1
        
        while leftSide <= rightSide:
            mid = (leftSide + rightSide) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                leftSide = mid + 1
            else:
                rightSide = mid - 1
        return -1
    
if __name__=="__main__":
    s = Solution()
    print(s.search([-1,0,3,5,9,12], 9))
    print(s.search([-1,0,3,5,9,12], 2))
    print(s.search([5], 5))
        