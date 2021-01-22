'''
Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.
'''

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w1, w2 = {}, {}
        def word_count(word):
            w = {}
            for i in range(len(word)):
                if word[i] not in w:
                    w[word[i]] = 1
                else:
                    w[word[i]] += 1
            return w
        w1, w2 = word_count(word1), word_count(word2)
        s = set(w2.values())
        for key in w1:
            if key not in w2:
                return False
        val1, val2 = list(w1.values()), list(w2.values())
        val1.sort()
        val2.sort()
        if val1 != val2:
            return False
        return True
