class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n<0:
            return 1/self.powerRe(x, -n)
        else:
            return self.powerRe(x, n)
    
    def powerRe(self, x, n):
        if n==0:
            return 1
        if n==1:
            return x
        if n%2==0:
            return self.powerRe(x*x, n/2)
        else:
            return self.powerRe(x*x, n/2)*x
