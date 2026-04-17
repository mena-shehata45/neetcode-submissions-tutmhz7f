class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_words = dict()
        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word in hash_words:
                hash_words[sorted_word].append(word) 

            else:
                hash_words[sorted_word] = [word]

        print(hash_words)
        return list(hash_words.values())


