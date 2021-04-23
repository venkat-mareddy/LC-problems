def twoSum(nums, target):
# Bruteforce code
    """
    n = len(nums)
    for i in range(0, n-1):
        for j in range(i+1, n):
           if(nums[i] == target - nums[j]):
               a = i
               b = j
               break 
    return[a,b]
    """
# O(n) solution
    h = {}
    for i, num in enumerate(nums):
       n = target - num
       if n not in h:
           h[num] = i
       else:
           return [h[n], i]
    
p = twoSum([-1, -2, -3, -4, -5], -8)
print(p)
