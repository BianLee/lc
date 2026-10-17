class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        std::unordered_set<int> nums_set; // use unordered_set over set
        for (int i = 0; i < nums.size(); i++) {
            if (nums_set.contains(nums[i])) {
                return true;
            }
            nums_set.insert(nums[i]);

        }
        return false;
    }
};
