class Solution:
    sum = 0
    def romanToInt(self, s: str) -> int:
        #First deal with instances with subtractrion
        if s == '': return sum
        if len(s) > 1 and s[0] == 'I' and s[1] == 'V':
            self.sum += 4
            self.romanToInt(s[2:])
        elif len(s) > 1 and s[0] == 'I' and s[1] == 'X':
            self.sum +=9
            self.romanToInt(s[2:])
        elif len(s) > 1 and s[0] == 'X' and s[1] == 'L':
            self.sum += 40
            self.romanToInt(s[2:])
        elif len(s) > 1 and s[0] == 'X' and s[1] == 'C':
            self.sum += 90
            self.romanToInt(s[2:])
        elif len(s) > 1 and s[0] == 'C' and s[1] == 'D':
            self.sum += 400
            self.romanToInt(s[2:])
        elif len(s) > 1 and s[0] == 'C' and s[1] == 'M':
            self.sum += 900
            self.romanToInt(s[2:])
        elif s[0] == 'I':
            self.sum += 1
            self.romanToInt(s[1:])
        elif s[0] == 'V':
            self.sum += 5
            self.romanToInt(s[1:])
        elif s[0] == 'X':
            self.sum += 10
            self.romanToInt(s[1:])
        elif s[0] == 'L':
            self.sum += 50
            self.romanToInt(s[1:])
        elif s[0] == 'C':
            self.sum += 100
            self.romanToInt(s[1:])
        elif s[0] == 'D':
            self.sum += 500
            self.romanToInt(s[1:])
        elif s[0] == 'M':
            self.sum += 1000
            self.romanToInt(s[1:])
        return self.sum