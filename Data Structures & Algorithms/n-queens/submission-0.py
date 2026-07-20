class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        total_nums = set(range(n))
        total_ans = []

        def solver(perms):
            k = len(perms)
            diag_plus = [perms[i] + i for i in range(k)]
            diag_minus = [perms[i] - i for i in range(k)]
            if k != len(set(diag_plus)) or k != len(set(diag_minus)):
                return

            if k == n:
                total_ans.append(
                    ['.' * r + 'Q' + '.' * (n - r - 1) for r in perms]
                )
                return

            for num in total_nums - set(perms):
                perms.append(num)
                solver(perms)
                perms.pop()

        solver([])
        return total_ans