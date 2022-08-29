# question : https://leetcode.com/problems/two-sum/
# video solution : https://youtu.be/KLlXCFG5TnA
# code solution : https://github.com/neetcode-gh/leetcode/blob/main/python/1-Two-Sum.py

numbers = [2, 7, 11, 15]
target_num = 9


def solution(nums: list[int], target: int) -> list[int]:
    prevMap = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i


sol = solution(numbers, target_num)

print(sol)
