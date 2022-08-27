# question : https://leetcode.com/problems/valid-anagram/
# video solution : https://youtu.be/9UtInBqnCgA
# code solution : https://github.com/neetcode-gh/leetcode/blob/main/python/242-Valid-Anagrams.py

s_word = "anagram"
t_word = "nagaram"


def solution_one(s: str, t: str) -> bool:

    if len(s) != len(t):
        return False

    s_sorted, t_sorted = sorted(s), sorted(t)

    for i in range(len(s_sorted)):
        if s_sorted[i] != t_sorted[i]:
            return False

    return True


def solution_two(s: str, t: str) -> bool:
    return True


sol1 = solution_one(s_word, t_word)
sol2 = solution_two(s_word, t_word)

print(sol1)
print(sol2)

