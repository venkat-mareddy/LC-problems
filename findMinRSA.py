def findMin(nums):

        n = len(nums)
        c = 5001
        for i in range(0, n):
            if(nums[i] < c):
                c = nums[i]
        return c

print(findMin([3, 4, 5, 1, 2]))
