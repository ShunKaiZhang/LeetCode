# python3
# A message containing letters from A-Z is being encoded to numbers using the following mapping:

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given an encoded message containing digits, determine the total number of ways to decode it.

# For example,
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

# The number of ways decoding "12" is 2.


# My solution
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '' or s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        res = set("123456")
        dp = [0 for i in range(len(s) + 1)]
        dp[0] = 1
        for i in range(1, len(s) + 1):
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]
            if i != 1 and s[i - 2:i] < "27" and s[i - 2:i] > "09":
                dp[i] += dp[i - 2]
        return dp[-1]



