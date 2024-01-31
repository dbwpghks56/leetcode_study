class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        answer = []

        while l <= r:
            sums = numbers[l] + numbers[r]

            if sums < target:
                l += 1
            
            elif sums > target:
                r -= 1

            else:
                answer.append(l+1)
                answer.append(r+1)

                return answer

        return answer
        