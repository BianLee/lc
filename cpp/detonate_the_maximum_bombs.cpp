#include <cmath>
class Solution {
public:


    // recursive DFS where we go down for each node and count 
    int dfs(int node, unordered_map<int, vector<int>>& adj, vector<bool>& visited) {
        visited[node] = true;
        int count = 1;
        for (int neighbor : adj[node]) { // for each node within tthe [] array
            if (!visited[neighbor]) { // if it hasn't been visited before
                count += dfs(neighbor, adj, visited);  // then recursively call dfs 
            }
        }
        return count; 
    }
    int maximumDetonation(vector<vector<int>>& bombs) {
        // the formula for finding the distance is 

        unordered_map<int, vector<int>> adj;

        for (int i = 0; i < bombs.size(); i++) {
            for (int j = i+1; j < bombs.size(); j++) {
                int x_one = bombs[i][0];
                int y_one = bombs[i][1];
                int one_radius = bombs[i][2];
                int x_two = bombs[j][0];
                int y_two = bombs[j][1];
                int two_radius = bombs[j][2];
                
                
                int dx = x_two - x_one;
                int dy = y_two - y_one;

                long long distanceSquared = 1LL * dx * dx + 1LL * dy * dy;

                if (1LL * one_radius * one_radius >= distanceSquared) {
                    // one_radius -> two_radius
                    adj[i].push_back(j);
                }
                if (1LL * two_radius * two_radius >= distanceSquared) {
                    adj[j].push_back(i);
                }
            }
        }
        
        // BFS -> use q
        // DFS -> use dequeue
        int maxBombs = 0;
        for (int i = 0; i < bombs.size(); i++) {
            vector<bool> visited(bombs.size(), false);// basically reset the visited bool

            int count = dfs(i, adj, visited);
            maxBombs = max(maxBombs, count);
        }




        return maxBombs; 
    }
};
