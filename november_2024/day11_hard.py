class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_number = 0
        current_sum = 0
        sign = 1

        for char in s:
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            elif char in '+-':
                current_sum += sign * current_number
                sign = 1 if char == '+' else -1
                current_number = 0
            elif char == '(':
                stack.append(current_sum)
                stack.append(sign)
                current_sum = 0
                sign = 1
            elif char == ')':
                current_sum += sign * current_number
                current_sum *= stack.pop()  # sign
                current_sum += stack.pop()  # last calculation
                current_number = 0
        
        current_sum += sign * current_number
        return current_sum