# question : https://leetcode.com/problems/two-sum/
# video solution : https://youtu.be/KLlXCFG5TnA
# code solution : https://github.com/neetcode-gh/leetcode/blob/main/python/1-Two-Sum.py

numbers = []


def solution(nums: list[int], target: int) -> list[int]:
    prevMap = {}

    for i, n in enumerate(nums):
        diff = target - n
        if target in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
