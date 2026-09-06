class Solution:
    def countGroups(self, position: list[int], speed: list[int], distance: int) -> int:
        n = len(position)
        v = []

        for i in range(n):
            if i == 0 or position[i] - position[i - 1] > distance:
                v.append(speed[i])
            else:
                v[-1] = speed[i]

        ans = 0
        m = float('inf')
        for i in range(len(v) - 1, -1, -1):
            if v[i] <= m:
                ans += 1
                m = v[i]

        return ans