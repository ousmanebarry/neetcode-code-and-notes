# question : https://leetcode.com/problems/contains-duplicate/
# video solution : https://youtu.be/3OamzN90kPg
# code solution : https://github.com/neetcode-gh/leetcode/blob/main/python/217-Contains-Duplicate.py


inp = [1, 2, 3, 1]


def solution_one(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


def solution_two(nums):
    sorted_nums = sorted(nums)

    for i in range(len(sorted_nums)):
        if i != len(sorted_nums) - 1 and sorted_nums[i] == sorted_nums[i+1]:
            return True
    return False


def solution_three(nums):
    nums_set = set()

    for i in nums:
        if i in nums_set:
            return True
        nums_set.add(i)

    return False


sol1 = solution_one(inp)
sol2 = solution_two(inp)
sol3 = solution_three(inp)


print(sol1, sol2, sol3)
