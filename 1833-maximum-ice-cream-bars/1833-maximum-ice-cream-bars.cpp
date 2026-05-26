class Solution {
public:
    int maxIceCream(vector<int>& costs, int coins) {
        int maxCost = 0;
        for (int cost : costs) {
            maxCost = max(maxCost, cost);
        }
        
        vector<int> count(maxCost + 1, 0);
        for (int cost : costs) {
            count[cost]++;
        }
        
        int bars = 0;
        for (int cost = 1; cost <= maxCost && coins > 0; cost++) {
            if (count[cost] > 0) {
                int canBuy = min(count[cost], coins / cost);
                bars += canBuy;
                coins -= canBuy * cost;
            }
        }
        
        return bars;
    }
};