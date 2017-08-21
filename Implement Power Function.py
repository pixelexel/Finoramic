class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer

    def pow(self, x, n, d):
        ans = 1
        base = x % d
        while n > 0:
            if n % 2 == 1:
                ans = (ans*base) % d
            n = n >> 1 #right shift to divide by half
            base = (base*base)%d
        return ans % d
