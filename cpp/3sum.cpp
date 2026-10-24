class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        std::set<vector<int>> numsSet;
        vector<vector<int>> ans; 

        sort(nums.begin(), nums.end()); // sorted to ascending order

        for (int i = 0; i < nums.size(); i++) {
            // cout << i;
            int l {i+1};
            int r = nums.size()-1;

            while (l < r) {
                int sum = nums[i] + nums[l] + nums[r];
                if (sum == 0) {
                    numsSet.insert({nums[i], nums[l], nums[r]});
                    l++;
                }
                else if (sum > 0) {
                    r--;
                }
                else { // sum < 0
                    l++;
                }
            }
        }
        for (vector<int> s : numsSet) {
            ans.push_back({s});
        }
        return ans; 
    
    }
};3
