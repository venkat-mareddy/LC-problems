def maxProductSubArray(nums):

      n = len(nums)
      
      max_Product = nums[0]
      temp_min = nums[0]
      temp_max = nums[0]
      for i in range(1, n):
         if(nums[i] < 0):
             s = temp_max
             temp_max = temp_min
             temp_min = s
         temp_max = max(nums[i], temp_max * nums[i])
         temp_min = min(nums[i],temp_min * nums[i])
         
         max_Product = max(max_Product, temp_max)
      return max_Product


nums = [-2, 0, -1]
print(maxProductSubArray(nums))
