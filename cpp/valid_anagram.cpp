class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }
        std::unordered_map<char, int> mapping_s;
        std::unordered_map<char, int> mapping_t;
        for (char c : s) {
            if (mapping_s.contains(c)) {
                mapping_s[c]+=1;
            }
            else {
                mapping_s[c] = 1;
            }
        }
        for (char c : t) {
            if (mapping_t.contains(c)) {
                mapping_t[c]+=1;
            }
            else {
                mapping_t[c] = 1;
            }
        }
        return mapping_s == mapping_t;

    }
};
