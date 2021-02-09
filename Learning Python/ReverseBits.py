class Solution:
    def reverseBits(self, n: int) -> int:
        counter = 32
        output = 0
        while counter >= 0:
            output += n % 1
            output = output << 1
            n = n >> 1
            counter -= 1
        return output
