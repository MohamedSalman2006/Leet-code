class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

# answer starts from here:
      
        for i in range(0, len(num)):                           #initialising looping through given list
            for j in range(i+1,len(nums)):                     #initialising loop 2 to get subsequent elements
                if nums[i]+nums[j]==target:                    #checking the two sum condition
                    list=[i, j]                                #getting the element indices and storing them in list
                    return list                                #returning output in specified format
