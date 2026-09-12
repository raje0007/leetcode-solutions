from bisect import bisect_right
from typing import List


class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:

        arr = []
        for i, (l, r, w) in enumerate(intervals):
            arr.append((l, r, w, i))


        arr.sort()

        n = len(arr)
        starts = [arr[i][0] for i in range(n)]
        next_index = [0] * n

        for i in range(n):
            r = arr[i][1]
            next_index[i] = bisect_right(starts, r)


        memo = {}

        def solve(i, count):
            if count == 4:
                return (0, ())

            if i == n:
                return (0, ())

            if (i, count) in memo:
                return memo[(i, count)]

            score1, indices1 = solve(i + 1, count)

            score2, indices2 = solve(next_index[i], count + 1)

            score2 += arr[i][2]

            indices2 = tuple(sorted((arr[i][3],) + indices2))

            if score2 > score1:
                answer = (score2, indices2)

            elif score1 > score2:
                answer = (score1, indices1)

            else:
                answer = min(
                    (score1, indices1),
                    (score2, indices2)
                )

            memo[(i, count)] = answer
            return answer

        score, answer = solve(0, 0)

        return list(answer)