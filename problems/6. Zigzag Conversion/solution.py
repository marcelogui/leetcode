class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        answer = ""
        rows = []
        for i in range(numRows):
            rows.append([])
        for i, letter in enumerate(s):
            index = i % ((numRows-1)*2)
            if index >= numRows:
                index = (numRows-1)*2 - index
            rows[index].append(letter)
        for j in rows:
            answer = answer + "".join(j)
        return answer


print(Solution().convert("PAYPALISHIRING", 3))
