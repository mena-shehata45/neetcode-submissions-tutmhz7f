class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)
        ch_found = False
        index = set()
        if len(s_list) != len(t_list):
            return False
        else:
            for i in range(len(s_list)):
                for j in range(len(t_list)):
                    if j in index:
                        continue
                    else:
                        if s_list[i] == t_list[j]:
                            index.add(j)
                            ch_found = True
                            break
                        else:
                            ch_found = False
                if ch_found == False:
                    return ch_found
            return ch_found


        