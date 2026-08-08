class Solution:
    def validSequence(self, word1: str, word2: str):
        n = len(word1)
        m = len(word2)

        # dp[i] = number of characters from the END of word2
        # that can be matched as a subsequence in word1[i:]
        dp = [0] * (n + 1)

        j = m - 1

        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1]

            if j >= 0 and word1[i] == word2[j]:
                dp[i] += 1
                j -= 1

        ans = []
        i = 0
        j = 0
        mismatch = False

        while i < n and j < m:

            # Exact match
            if word1[i] == word2[j]:
                ans.append(i)
                i += 1
                j += 1

            # Use the one allowed mismatch
            elif not mismatch and dp[i + 1] >= m - j - 1:
                ans.append(i)
                i += 1
                j += 1
                mismatch = True

            else:
                i += 1

        if j == m:
            return ans

        return []