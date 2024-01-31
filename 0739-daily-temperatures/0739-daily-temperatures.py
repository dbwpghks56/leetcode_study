class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)

        for cur_day, cur_temp in enumerate(temperatures):
            while stack and stack[-1][1] < cur_temp:
                prev_day, _ = stack.pop()
                answer[prev_day] = cur_day - prev_day
            stack.append((cur_day, cur_temp))
        
        return answer