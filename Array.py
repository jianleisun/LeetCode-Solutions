
'''
REMARKS

Problem 1:

c1 = [1, 6, 7, 10, 13, 28, 32, 41, 58, 63]
c2 = [[13, 17, 18, 21, 32], [7, 11, 13, 14, 28], [1, 5, 6, 8, 15, 16]]
c3 = [[13, 32], [7, 13, 28], [1,6]]
Then here is your solution for Python 2:

c3 = [filter(lambda x: x in c1, sublist) for sublist in c2]
In Python 3 filter returns an iterable instead of list, so you need to wrap filter calls with list():

c3 = [list(filter(lambda x: x in c1, sublist)) for sublist in c2]

Problem 2:

Pure list comprehension version

>>> c1 = [1, 6, 7, 10, 13, 28, 32, 41, 58, 63]
>>> c2 = [[13, 17, 18, 21, 32], [7, 11, 13, 14, 28], [1, 5, 6, 8, 15, 16]]
>>> c1set = frozenset(c1)
Flatten variant:

>>> [n for lst in c2 for n in lst if n in c1set]
[13, 32, 7, 13, 28, 1, 6]
Nested variant:

>>> [[n for n in lst if n in c1set] for lst in c2]
[[13, 32], [7, 13, 28], [1, 6]]






'''

## --------------------------
			Easy
## --------------------------

'''



# 448. Find All Numbers Disappeared in an Array  

# approach:  negative labeling

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]

'''
class Solution(object):
	def findDisappearedNumbers(self, nums):
		for i in range(len(nums)):
			nums[abs(nums[i])-1] = - abs(nums[abs(nums[i])-1])
		return [ i+1 for i in range(len(nums)) if nums[i] > 0 ]

# space: O(n)
# time: O(1)



# 453. Minimum Moves to Equal Array Elements  

'''

Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.

Example:

Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

'''

# solution 1 - sorting the array

class Solution(object):
    def minMoves(self, nums):
        nums.sort()
        c = 0
        for i in range(len(nums)-1, 0, -1):
        	if(nums[i] == nums[0]):
        		break
        	else:
        		c += (nums[i] - nums[0])
        return c

# time O(nlogn)
# space O(1)

# solution 2 - convert the problem to a mathetmetical equation

class Solution(object):
	def minMoves(self, sums):
		return (sum(sums) - len(sums) * min(sums))

# time O(n)
# space O(1)



# 26. Remove Duplicates from Sorted Array

# approach: two pointers

'''

Given a sorted array, remove the duplicates in place such that each element 
appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with 
constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums 
being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

'''

class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        p1 = 0
        for i in range(1,len(nums)):
            if(nums[p1] != nums[i]):
                nums[p1+1] = nums[i]
                p1 += 1
        return p1+1

# time O(n)
# space O(1)



# 88. Merge Sorted Array  

'''

approach: two pointers

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 
as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or 
equal to m + n) to hold additional elements from nums2. 
The number of elements initialized in nums1 and nums2 are m and n respectively.

'''
class Solution(object):
	def merge(self, nums1, m, nums2, n):
		while m > 0 and n > 0:
			if nums1[m-1] > nums2[n-1]:
				nums1[m+n-1] = nums1[m-1]
				m -= 1
			else:
				nums1[m+n-1] = nums2[n-1]
				n -= 1
		if n > 0:
			nums1[:n] = nums2[:n]
		return nums1

# time: O(n)
# space: O(1)



# 189. Rotate Array  

# Approach: pay attention to "k == 0"

'''
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] 
is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different 
ways to solve this problem.

[show hint]

Related problem: Reverse Words in a String II
'''
'''

'''

# brute force [Time Limit Exceeded]
class Solution(object):
	def rotate(self, nums, k):
		if k > len(nums):
			k = k % len(nums)
		while k > 0:
			temp = nums[len(nums)-1]
			for i in range(len(nums)-2, -1, -1):
				nums[i+1] = nums[i]
			nums[0] = temp
			k -= 1
		return nums


# time: O(nk)
# space: O(1)

# extra array space
class Solution(object):
	def rotate(self, nums, k):
		if k > len(nums):
			k = k % len(nums)
		if k != 0:	
			n = len(nums)
			temp = nums[-k:]
			nums[k:] = nums[:n-k]
			nums[:k] = temp

# time: O(n)
# space: O(k)


# reverse three times
class Solution(object):
	# define the reserve function
	def reverse(self, nums, start, end):
		while start < end:
			nums[start], nums[end] = nums[end], nums[start]
			start += 1
			end -= 1
	def rotate(self, nums, k):
		k %= len(nums)
		if k != 0:
			self.reverse(nums, 0, len(nums)-1)
			self.reverse(nums, 0, k-1)
			self.reverse(nums, k, len(nums)-1)

# time: O(n)
# space: O(1)






## --------------------------
			Medium
## --------------------------




# 442. Find All Duplicates in an Array

# approach:  negative labeling

'''

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), 
some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]

'''

class Solution(object):
	def findDuplicates(self, nums):
		ret = []
		for i in nums:
			if nums[abs(i)-1] > 0:
				nums[abs(i)-1] = - nums[abs(i)-1]
			else:
				ret.append(abs(i))
		return ret




# 462. Minimum Moves to Equal Array Elements II

# approach: use median

'''

Given a non-empty integer array, find the minimum number of moves required to 
make all array elements equal, where a move is incrementing a selected element 
by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.

Example:

Input:
[1,2,3]

Output:
2

Explanation:
Only two moves are needed (remember each move increments or decrements one element):

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]

'''

class Solution(object):
    def minMoves2(self, nums):
        median = sorted(nums)[int(len(nums)/2)]
        return sum([abs(i-median) for i in nums])


$ time: O(nlogn)
# space: O(1)



# 238. Product of Array Except Self  

'''

Given an array of n integers where n > 1, nums, return an array 
output such that output[i] is equal to the product of all the elements 
of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? 
(Note: The output array does not count as extra space for 
the purpose of space complexity analysis.)

'''

class Solution(object):
	def productExceptSelf(self, nums):
		if not nums:
			return []
		left = [1 for i in range(len(nums))]
		# compute the left product
		for i in range(len(nums)-1):
			left[i+1] = left[i] * nums[i]

		right = 1
		# compute the right product
		for i in range(len(nums)-1, 0, -1):
			right = right * nums[i]
			left[i-1] = left[i-1] * right

		return left

# time: O(n)
# space: O(1)


# 384. Shuffle an Array  

'''
Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();

'''

class Solution(object):

    def __init__(self, nums):
        self._nums = nums

    def reset(self):
        return self._nums

    def shuffle(self):
        import random
        # create a copy of the list
        nums = list(self._nums)
        for i in range(len(nums)):
            j = random.randint(i, len(nums)-1)
            nums[i], nums[j] =  nums[j], nums[i]
        return nums


# 360. Sort Transformed Array

'''
Given a sorted array of integers nums and integer values a, 
b and c. Apply a function of the form f(x) = ax2 + bx + c 
to each element x in the array.

The returned array must be in sorted order.

Expected time complexity: O(n)

Example:
nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5,

Result: [3, 9, 15, 33]

nums = [-4, -2, 2, 4], a = -1, b = 3, c = 5

Result: [-23, -5, 1, 7]
'''

































