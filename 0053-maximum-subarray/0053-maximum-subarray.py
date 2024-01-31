class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')  # 초기 최대값을 음의 무한대로 설정
        current_sum = 0  # 현재 서브어레이의 합을 저장하는 변수

        for num in nums:
            # 현재 숫자를 현재 서브어레이에 추가하거나, 새로운 서브어레이를 시작하는 것 중 큰 값을 선택
            current_sum = max(num, current_sum + num)
            # 최대 서브어레이 합 갱신
            max_sum = max(max_sum, current_sum)

        return max_sum
