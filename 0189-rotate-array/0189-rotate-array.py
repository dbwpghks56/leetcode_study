class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        result = deque(nums)
        result.rotate(k)
        result = list(result)
        n = len(nums)
        
        nums[:n] = result