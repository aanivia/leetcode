class Solution(object):
    def isVaild(self, s: str) -> bool:
        stack = ["?"]
        dic = {"(": ")", "[": "]", "{": "}"}
        for i in s:
            if i in dic:
                stack.append(i)
            elif i != dic.get(stack.pop()):
                return False
        return len(stack) == 1
