class Solution {
public:
    int longestConsecutive(vector<int>& nums) {

        unordered_set<int> numsSet;
        for (int n : nums) {
            numsSet.insert(n);
        }
        int maxCount { 0 }; 

        for (int n : numsSet) {
            if (numsSet.contains(n - 1)) { // only start counting if it['s the front
                continue; 
            }
            int counter = 1;
            while (numsSet.contains(n + counter)) {
                counter++;
            }
            maxCount = max(maxCount, counter);

        }
        return maxCount; 
    }
};
