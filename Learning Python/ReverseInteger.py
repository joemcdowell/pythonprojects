class Solution:
    def Convert(self, string):
        list1 = []
        list1[:0] = string
        return list1

    def reverse(self, x: int) -> int:
        stack = self.Convert(str(x))
        isNegative = False
        neg = '-'
        if stack[0] == '-':
            stack = stack[1:]
            isNegative = True
        output = ''
        k = len(stack)
        while (k>0):
            output += stack.pop()
            k -= 1
        if isNegative: neg + output
        outputInt = int(output)
        if outputInt > 2 ** 31 - 1 or outputInt < -2 ** 31: return 0
        return outputInt