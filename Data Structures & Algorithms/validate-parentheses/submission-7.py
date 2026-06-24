class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        for val in s:
            if val == "[" or val == "{" or val == "(":
                arr.append(val)
            else:
                if arr == []:
                    return False

                elif val == "]":
                    if arr[-1] != "[":
                        return False
                    arr.pop()

                elif val == "}":
                    if arr[-1] != "{":
                        return False
                    arr.pop()

                else:
                    if arr[-1] != "(":
                        return False
                    arr.pop()

        return arr == []