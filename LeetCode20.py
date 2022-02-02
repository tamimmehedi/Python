class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        pairs = {"}":"{",")":"(","]":"["}
        stack=[]
        for c in s:
            if c not in pairs.keys():
                stack.append(c)
            else:
                if len(stack)==0 or stack[-1]!=pairs[c]:
                    return False
                else:
                    stack.pop()
        return len(stack)==0
