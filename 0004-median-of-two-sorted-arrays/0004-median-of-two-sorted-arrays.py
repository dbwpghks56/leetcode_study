class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = sorted(nums1 + nums2)
        n = len(nums3)
        median = (nums3[n//2] + nums3[n//2-1])/2 if n%2==0 else nums3[n//2]

        return median