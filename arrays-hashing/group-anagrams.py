# question :
# video solution :
# code solution :

inp = ["eat", "tea", "tan", "ate", "nat", "bat"]


def solution(strs: list[str]) -> list[list[str]]:
    str_count, new_list = {}, []

    for i in strs:
        for j in range(len(i)):
            str_count[i[j]] = 1 + str_count.get(i[j], 0)
        new_list.append(str_count)
        str_count = {}

    return new_list


sol = solution(inp)

print(sol)
