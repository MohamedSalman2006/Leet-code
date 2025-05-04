class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

# answer starts from here:
      
        for i in nums:                           #initialising looping through given list
            for j in range(1,len(nums)):         #initialising loop 2 to get subsequent elements
                if i+nums[j]==target:            #checking the two sum condition
                    list=[nums.index(i), j]      #getting the element indices and storing them in list
                    return list                  #returning output in specified format
