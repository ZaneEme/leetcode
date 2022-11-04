class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        # return target if exists, if not return index of where it should be
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
    
if __name__=="__main__":
    S = Solution()
    
    print(S.searchInsert([1,3,5,6], 5))
    print(S.searchInsert([1,3,5,6], 2))
    print(S.searchInsert([1,3,5,6], 7))
    print(S.searchInsert([1,3,5,6], 0))