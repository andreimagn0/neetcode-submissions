from collections import deque
import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        we implement a stack
        we go through the entire tokens list
        every time we see a number, we push it to the stack
        once we see an operation, we do that operation on the remaining numbers in the stack, and push the result
        we return the final value remaining the stack
        '''

        stack = deque()
        OPERATION_MAP = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul
        }
        for token in tokens:
            if token in OPERATION_MAP:
                b = stack.pop()
                a = stack.pop()
                result = OPERATION_MAP[token](a, b)
                stack.append(result)
            elif token == "/":
                b = stack.pop()
                a = stack.pop()
                result = int(a / b)  # int() truncates decimals toward zero
                stack.append(result)
            else:
                stack.append(int(token))
            
        return stack.pop()
