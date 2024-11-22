class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_number = 0
        sign = '+'

        for i, char in enumerate(s):
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            
            if char in '+-*/' or i == len(s) - 1:
                if sign == '+':
                    stack.append(current_number)
                elif sign == '-':
                    stack.append(-current_number)
                elif sign == '*':
                    stack.append(stack.pop() * current_number)
                elif sign == '/':
                    stack.append(int(stack.pop() / current_number))
                
                sign = char
                current_number = 0
        
        return sum(stack)