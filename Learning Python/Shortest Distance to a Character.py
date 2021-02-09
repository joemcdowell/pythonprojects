class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        answer = []
        revStr = s[::-1]
        print(revStr)
        # full pass through
        for w in range(0, len(s)):
            answer.append(abs(w - s.index(c, w)))

        # reverse pass through and replace if lower
        print(answer)
        answer.reverse()
        for v in range(0, len(s)):
            if answer[v] > abs(v - revStr.index(c, v)):
                answer[v] = abs(v - revStr.index(c, v))
        answer.reverse()

        return answer