class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, 0
        min_length = float('inf')
        current_sum = 0

        while right < n:
            current_sum += nums[right]

            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1

            right += 1

        return min_length if min_length != float('inf') else 0
