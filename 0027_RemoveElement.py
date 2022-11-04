# remove "val" inline in list

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        print(nums)
        return count
    
    
if __name__=="__main__":
    s = Solution()
    print(s.removeElement([3,2,2,3], 3))
    print(s.removeElement([0,1,2,2,3,0,4,2], 2))