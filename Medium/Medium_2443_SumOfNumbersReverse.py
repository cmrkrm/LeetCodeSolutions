class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for n in range(num//2,num+1):
            if n + self.rev(n) == num:
                return True
        return False
                                             
    def rev(self, num: int, reverse = 0) -> int:
        while num != 0:
            reverse = (reverse * 10) + (num % 10)
            num //= 10
        return reverse