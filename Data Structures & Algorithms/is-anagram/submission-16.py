class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        occ = dict()
        occ2 = dict()
        for c in s:
            if c in occ.keys():
                occ[c] +=1
            else:
                occ[c] = 1

        for c in t:
            if c in occ2.keys():
                occ2[c] +=1
            else:
                occ2[c] = 1

        if occ == occ2:
            return True 
            

        return False

