/*
 * 1. Two Sum
 * Link: https://leetcode.com/problems/two-sum/
 * Difficulty: Easy
 * Time: O(n)   Space: O(n)
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen; // value -> index
        for (int i = 0; i < (int)nums.size(); i++) {
            int need = target - nums[i];
            if (seen.count(need)) return {seen[need], i};
            seen[nums[i]] = i;
        }
        return {};
    }
};

int main() {
    Solution s;
    vector<int> a = {2, 7, 11, 15};
    assert((s.twoSum(a, 9) == vector<int>{0, 1}));
    vector<int> b = {3, 2, 4};
    assert((s.twoSum(b, 6) == vector<int>{1, 2}));
    cout << "ok\n";
    return 0;
}
