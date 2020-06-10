# Day 10
# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.

# Example 1:

# Input: [1,3,5,6], 5
# Output: 2
# class Solution:
def searchInsert(self, nums,target):
    idx =0
    for i in range(len(nums)):
        if(nums[i]==target):
            idx = nums.index(target)
        else:
            if(nums[i]<target):
                idx+=1
    return idx
print(searchInsert(0,[1,2,3,5],8))