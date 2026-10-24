class Solution {
public:

    vector<vector<int>> ans; 
    void backtrack(int index, vector<int>& current, vector<int>& candidates, int target) {
        // base case
        int sum {0};
        for (int n : current) {
            sum += n;
        }
        if (sum == target) {
            ans.push_back(current);
            return;
        }
        if (sum > target) {
            return;
        }

        for (int i = index; i < candidates.size(); i++) {
            current.push_back(candidates[i]);
            backtrack(i, current, candidates, target);
            current.pop_back();
        }
    } 
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> current;
        backtrack(0, current, candidates, target);
        return ans; 
    }
};
