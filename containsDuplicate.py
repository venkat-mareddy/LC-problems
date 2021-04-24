def containsDuplicate(nums):
        #bruteforce solution
        """
        li = list(set(nums))
        o1 = sorted(li, key = nums.index)
        if(nums == o1):
            return False
        else:
            return True
        """
        #simple logic
        if(len(nums) == len(set(nums))):
            return False
        else:
            return True


d = containsDuplicate([3, 1])
print(d)
