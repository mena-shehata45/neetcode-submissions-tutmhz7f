class Solution:
    def isPalindrome(self, s: str) -> bool:

        pali = False
        newS = ""
        for c in s:
            if(c.isalnum()):
                newS += c.lower()

        print(newS)
        return newS == newS[::-1]
        