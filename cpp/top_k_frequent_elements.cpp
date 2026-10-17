class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<vector<int>> arr(nums.size());
        std::unordered_map<int, int> mapping; 
        for (int n : nums) {
            if (mapping.contains(n)) {
                mapping[n]+=1;
            }
            else{
                mapping[n]=1;
            }
        }
        vector<int> temp; 
        for (auto& n : mapping) {
            // cout << n.first << "," << n.second << endl;
            arr[n.second-1].push_back(n.first);
        }
        vector<int> ans; 

        for (int i = arr.size()-1; i >= 0; i--) { // iterate backwards 
            for (int j = 0; j < arr[i].size(); j++) {
                ans.push_back(arr[i][j]);
                if (ans.size() == k) {
                    return ans; 
                }
            }
        }

        return ans;  
    };
};
