class Solution:
    def isHappy(self, n: int) -> bool:
        current_no = n
        iterated_no = []
        while current_no != 1:
            if current_no not in iterated_no:
                iterated_no.append(current_no)
                current_no = sum([int(x)**2 for x in str(current_no)])
            else: return False
        return True