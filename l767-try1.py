class Solution:
    def reorganizeString(self, s: str) -> str:

        # tried (4/12/25)(1029-1050pm)(Sat) 

        # compare current char with the char next to it
        # then flip it with the char after the next

        # or, compare with the char before it and swap it with the next
        
        s = list(s)
        for i in range(1, len(s)-1):
            if s[i] == s[i-1]:
                temp = s[i]
                s[i] = s[i+1]
                s[i+1] = temp
            else:
                return ""
        return "".join(s)
        
