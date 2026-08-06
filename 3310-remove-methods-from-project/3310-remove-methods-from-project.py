from collections import deque

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        suspicious = [False] * n

        for u, v in invocations:
            graph[u].append(v)

        # Find all suspicious methods (reachable from k)
        q = deque([k])
        suspicious[k] = True

        while q:
            u = q.popleft()
            for v in graph[u]:
                if not suspicious[v]:
                    suspicious[v] = True
                    q.append(v)

        # If any non-suspicious method invokes a suspicious one,
        # removal is impossible.
        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(range(n))

        # Return all remaining (non-suspicious) methods
        return [i for i in range(n) if not suspicious[i]]
        