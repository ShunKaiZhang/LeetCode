# python3
# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

# Strings consists of lowercase English letters only and the length of both strings s
# and p will not be larger than 20,100.

# The order of output does not matter.

# Example 1:

# Input:
# s: "cbaebabacd" p: "abc"

# Output:
# [0, 6]

# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input:
# s: "abab" p: "ab"

# Output:
# [0, 1, 2]

# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".


# My solution
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        p_dict = {}
        s_dict = {}
        for i in range(len(p)):
            if p[i] in p_dict:
                p_dict[p[i]] += 1
            else:
                p_dict[p[i]] = 1
            if s[i] in s_dict:
                s_dict[s[i]] += 1
            else:
                s_dict[s[i]] = 1
        out = []
        if p_dict == s_dict:
            out.append(0)
        i += 1
        while i < len(s):
            if s_dict[s[i - len(p)]] == 1:
                s_dict.pop(s[i - len(p)])
            else:
                s_dict[s[i - len(p)]] -= 1
            if s[i] in s_dict:
                s_dict[s[i]] += 1
            else:
                s_dict[s[i]] = 1
            if p_dict == s_dict:
                out.append(i - len(p) + 1)
            i += 1

        return out