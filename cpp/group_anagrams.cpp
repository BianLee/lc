class Solution {
public:
    // this means, the return shape is vector of vector<string>
    vector<vector<string>> groupAnagrams(vector<string>& strs) { // pass reference

        // unorderd_map where key is the string mapping (count of each letter), and the value is the list of original strings 

        std::unordered_map<string, vector<string>> mapping;

        vector<vector<string>> answer; 

        for (string s : strs) {
            string key = s;
            sort(key.begin(), key.end()); // This sorts the characters in the string key in ascending order (alphabetically for lowercase letters).
            mapping[key].push_back(s);
        }
        
        for (auto& entry : mapping) {
            answer.push_back(entry.second);
        }
        return answer;
    }
};
