def maxSubArray(nums):

      n = len(nums)
      temp = [0] * n
      temp[0] = nums[0]
      for i in range(1, n):
         temp[i] = max(temp[i-1] + nums[i], nums[i])
      return max(temp) 

nums = [5, 4 -1, 7, 8]
print(maxSubArray(nums))
