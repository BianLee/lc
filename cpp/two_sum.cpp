#include <unordered_map>

class Solution {
public:


    std::unordered_map<int, int> hash_map; // string : int
    // < diff, index>
    // <7, 0>
    // <2, 1>

    vector<int> twoSum(vector<int>& nums, int target) {
        for (int i = 0; i < nums.size(); i++) { // iterate over the nums array
            if (hash_map.contains(nums[i])) {
                return {i, hash_map[nums[i]]};
            }
            int diff = target - nums[i];
            hash_map[diff] = i;
        }
        return {};


        /*
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i; j < nums.size(); j++) {
                if (nums[i] + nums[j] == target && i!=j) {
                    return {i,j};
                }
            }
        }
        return {}; 
        
        */

    }
};
