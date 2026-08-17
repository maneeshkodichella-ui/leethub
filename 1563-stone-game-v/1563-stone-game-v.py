import bisect

class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        def rangeSum(i, j):
            return prefix[j + 1] - prefix[i]

        dp = [[0] * n for _ in range(n)]
        # maxLeft[i][j] = max over k in [i,j] of dp[i][k] + sum(i,k)
        # maxRight[i][j] = max over k in [i,j] of dp[k][j] + sum(k,j)
        maxLeft = [[0] * n for _ in range(n)]
        maxRight = [[0] * n for _ in range(n)]

        for i in range(n):
            maxLeft[i][i] = stoneValue[i]
            maxRight[i][i] = stoneValue[i]

        for length in range(2, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                # find split point via binary search on prefix sums
                # we want largest k such that rangeSum(i,k) <= rangeSum(k+1,j)
                lo, hi = i, j - 1
                # binary search for the boundary where left half <= right half
                pos = i - 1
                l, r = i, j - 1
                while l <= r:
                    mid = (l + r) // 2
                    if rangeSum(i, mid) <= rangeSum(mid + 1, j):
                        pos = mid
                        l = mid + 1
                    else:
                        r = mid - 1

                best = 0
                # pos is the largest k where left <= right (left gets kept, possibly tie)
                if pos >= i:
                    left = rangeSum(i, pos)
                    right = rangeSum(pos + 1, j)
                    if left == right:
                        best = max(best, maxLeft[i][pos], maxRight[pos + 1][j])
                    else:
                        best = max(best, maxLeft[i][pos])
                # the split just after pos: right half becomes the smaller one
                if pos + 1 <= j - 1:
                    best = max(best, maxRight[pos + 2][j] if pos + 2 <= j else 0)
                if pos + 1 <= j - 1:
                    k = pos + 1
                    left = rangeSum(i, k)
                    right = rangeSum(k + 1, j)
                    if left < right:
                        best = max(best, maxRight[k + 1][j])

                dp[i][j] = best
                maxLeft[i][j] = max(maxLeft[i][j - 1], dp[i][j] + rangeSum(i, j))
                maxRight[i][j] = max(maxRight[i + 1][j], dp[i][j] + rangeSum(i, j))

        return dp[0][n - 1]