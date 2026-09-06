class Solution {
public:
    int minCost(vector<vector<int>>& grid, int k) {
        int m = grid.size(), n = grid[0].size();
        if (m == 1 && n == 1) return grid[0][0];

        const long long INF = 4e18;
        int dr[] = {-1, 1, 0, 0}, dc[] = {0, 0, -1, 1};

        auto inside = [&](int r, int c) {
            return r >= 0 && r < m && c >= 0 && c < n;
        };

        auto id = [&](int r, int c, int d, int t) {
            return ((((long long)r * n + c) * 4 + d) * (k + 1) + t);
        };

        vector<long long> dist((long long)m * n * 4 * (k + 1), INF);
        using T = tuple<long long, int, int, int, int>;
        priority_queue<T, vector<T>, greater<T>> pq;

        auto push = [&](int r, int c, int d, int t, long long cost) {
            auto z = id(r, c, d, t);
            if (cost >= dist[z]) return;
            dist[z] = cost;
            pq.emplace(cost, r, c, d, t);
        };

        for (int d = 0; d < 4; ++d) {
            int r = dr[d], c = dc[d];
            if (inside(r, c))
                push(r, c, d, 0, (long long)grid[0][0] + grid[r][c]);
        }

        while (!pq.empty()) {
            auto [cost, r, c, d, t] = pq.top();
            pq.pop();

            if (cost != dist[id(r, c, d, t)]) continue;
            if (r == m - 1 && c == n - 1) return cost;

            for (int nd = 0; nd < 4; ++nd) {
                int nr = r + dr[nd], nc = c + dc[nd];
                int nt = t + (nd != d);

                if (inside(nr, nc) && nt <= k)
                    push(nr, nc, nd, nt, cost + grid[nr][nc]);
            }
        }

        return -1;
    }
};