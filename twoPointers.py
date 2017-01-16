# 349. Intersection of Two Arrays  
# approach: set

'''

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.

'''

class Solution(object):
	def intersection(self, nums1, nums2):
		return list(set(nums1) & set(nums2))

# time O(len(nums1) + len(nums2))
# space O(1)




# 350. Intersection of Two Arrays II

'''

ven two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.

Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that 
you cannot load all elements into the memory at once?

'''

# 1) unsorted + hashMap (Counter)
class Solution(object):
	def intersect(self, nums1, nums2):
		return list((collections.Counter(nums1) & collections.Counter(nums2)).elements())

# time: O(m+n)
# space: O(1)


# 2) unsorted/sorted + two pointers + large datasets on disk
class Solution(object):
    def intersect(self, nums1, nums2):
        p1 = 0
        p2 = 0
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        res = []

        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                res.append(nums1[p1])
                p1 += 1
                p2 += 1

        return res

# time: unsorted, O(max(m,n) * log(max(m,n)))
# time: sorted O(m+n)
# space: O(5)

# 3) binary search




# 27. Remove Element

# approach: two pointers

'''

Given an array and a value, remove all instances of that value in place and 
return the new length.

Do not allocate extra space for another array, you must do this in place 
with constant memory.

The order of elements can be changed. It doesn't matter what you leave 
beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.

'''
class Solution(object):
	def removeElement(self, nums, val):
		if len(nums) == 0:
			return 0
		p1 = 0
		for i in range(len(nums)):
			if(nums[i] != val):
				nums[p1] = nums[i]
				p1 += 1
		return p1


# time: O(n)
# space: O(1)



# 167. Two Sum II - Input array is sorted  

'''

Given an array of integers that is already sorted in ascending order, 
find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that 
they add up to the target, where index1 must be less than index2. 
Please note that your returned answers (both index1 and index2) are 
not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

'''

# two pointers
class Solution(object):
	def twoSum(self, numbers, target):
		p1, p2 = 0, len(numbers) - 1
		while p1 < p2:
			if numbers[p1] + numbers[p2] == target:
				return [p1+1, p2+1]
			elif numbers[p1] + numbers[p2] > target:
				p2 -= 1
			else:
				p1 += 1

# time: (n)
# space: (1)

# dictionary
class Solution(object):
	def twoSum(self, numbers, target):
		dict = {}
		for i, num in enumerate(numbers):
			if (target-num) in dict:
				return [dict[target-num]+1, i+1]
			dict[num] = i

# time: (n)
# space: (1)
















