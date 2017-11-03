# python3
# Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of
# 1's in their binary representation and return them as an array.

# Example:
# For num = 5 you should return [0,1,1,2,1,2].

# Follow up:

# It is very easy to come up with a solution with run time O(n*sizeof(integer)).
# But can you do it in linear time O(n) /possibly in a single pass?
# Space complexity should be O(n).
# Can you do it like a boss?
# Do it without using any builtin function like __builtin_popcount in c++ or in any other language.


# My solution
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        out = []
        re_to_one = 1
        for i in range(num + 1):
            if i == 0:
                out.append(0)
            elif i == re_to_one:
                out.append(1)
                re_to_one *= 2
            else:
                out.append(out[i - re_to_one] + 1)
        return out

