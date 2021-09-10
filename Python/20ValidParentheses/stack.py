class Solution:
    def isValid(self, s: str) -> bool:
        mapk = {"(":")", "{":"}", "[":"]"}
        st = []
        for x in s:
            #print(x, st)
            if x == "(" or x == "{" or x=="[":
                st.append(x)
            if x == ")" or x == "}" or x == "]":
                if len(st) == 0:
                    return False
                y = st.pop()
                if x!=mapk[y]:
                    return False
        if len(st)>0:
            return False
        return True