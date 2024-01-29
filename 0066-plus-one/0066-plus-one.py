class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        digits2 = []

        s = int(''.join(map(str, digits))) + 1

        while s:
            d,m = divmod(s, 10)
            s = d
            digits2.insert(0,m)

        return digits2