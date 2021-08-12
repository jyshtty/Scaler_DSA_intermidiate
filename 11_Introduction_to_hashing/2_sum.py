"""
2 Sum
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 < index2. Please note that your returned answers (both index1 and index2 ) are not zero-based. Put both these numbers in order in an array and return the array from your function ( Looking at the function signature will make things clearer ). Note that, if no pair exists, return empty list.

If multiple solutions exist, output the one where index2 is minimum. If there are multiple solutions with the minimum index2, choose the one with minimum index1 out of them.

Input: [2, 7, 11, 15], target=9
Output: index1 = 1, index2 = 2
"""

class Solution:
    def twoSum(self, arr, target):
        dict01 = {}
        for i in range(len(arr)):
            if (target - arr[i]) not in dict01:
                dict01[arr[i]]  = i
            else:
                return [dict01[target - arr[i]]+1, i+1]
        return 0

if __name__ == "__main__" :
    arr = [2, 7, 11, 15]
    target = 9
    obj = Solution()
    print(obj.twoSum(arr, target))