class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        d = []

        for token in tokens:
            if token == "+":
                first = d.pop()
                second = d.pop()
                d.append(second + first)
                
            elif token == "-":
                first = d.pop()
                second = d.pop()
                d.append(second - first)
                
            elif token == "*":
                first = d.pop()
                second = d.pop()
                d.append(second * first)

            elif token == "/":
                first = d.pop()
                second = d.pop()
            
                d.append(math.trunc(second / first))

            else:
                d.append(int(token))

        return d.pop()

        