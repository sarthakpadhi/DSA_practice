class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int ans = 0;
        int minSoFar = pow(10, 4);

        for(auto p : prices){
            minSoFar = min(minSoFar, p);
            ans = max(ans, p - minSoFar);
        }
        return ans;
    }
};
