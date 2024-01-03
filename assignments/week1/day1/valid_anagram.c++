class Solution {
public:
    bool isAnagram(string s, string t) {
        //check to see if the two strings are the same size
        //use 2 hashmaps to insert the letters along with how many of each letter
        //check if both the hashmaps are equal to each other in terms of numbers
        //return true if it's the same
        //return false otherwise
        if (s.size() != t.size()) {
            return false;
        }

        unordered_map<char, int> letters1;
        unordered_map<char, int> letters2;

        for (int i = 0; i < s.size(); i++) {
            letters1[s[i]]++;
            letters2[t[i]]++;
        }

        for (int i = 0; i < letters1.size(); i++) {
            if (letters1[i] != letters2[i]) {
                return false;
            }
        }
        return true;
    }
};