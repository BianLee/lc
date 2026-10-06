class Solution {
public:
    bool isValid(string s) {
        stack<char> character_stack;
        unordered_map<char, char> hashMapLookup = {
            {')', '('},
            {']', '['},
            {'}', '{'},
        };

        // stack is a LIFO = last in, first out

        // so if you have (([])) then the stack goes
        // ( -> (( -> (([ -> (( -> (, 
        for (char c : s) {
            if (c == '(' || c == '[' || c == '{') {
                character_stack.push(c);
            }
            else {
                if (character_stack.empty()) { // if the stack is empty
                    return false;
                }
                else {
                    char top_value = character_stack.top();
                    if (top_value == hashMapLookup[c]) {
                        character_stack.pop(); 
                    }
                    else {
                        character_stack.push(c);
                    }
                }
            }
        }
        /* 
        stack<char> copy_of_character_stack = character_stack; 
        cout << copy_of_character_stack.size() << endl;
        for (int i = 0; i < copy_of_character_stack.size(); i++) {
            cout << copy_of_character_stack.top() << endl;
            copy_of_character_stack.pop();
        }
        */ 
        if (character_stack.empty()) {
            return true;
        }
        return false; 
    }
};      
