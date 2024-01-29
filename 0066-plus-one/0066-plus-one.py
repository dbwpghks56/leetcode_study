class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        digits2 = []

        for digi in digits:
            s += str(digi)

        s = int(s) + 1

        while s:
            d,m = divmod(s, 10)
            s = d
            digits2.insert(0,m)

        return digits2