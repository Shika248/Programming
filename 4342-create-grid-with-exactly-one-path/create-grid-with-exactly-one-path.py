class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        res = [['#'] * n for _ in range(m)]

        for i in range(n):
            res[0][i] = '.'

        for i in range(1, m):
            res[i][n - 1] = '.'

        return [''.join(row) for row in res]
        