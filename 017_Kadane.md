

# 练习

| 题目名称                                      | 难度   |思路|
|---------------------------------------------|--------|---|
| [53. 最大子数组和](https://leetcode.cn/problems/maximum-subarray/description)| 中等+ | dp[i] = max(nums[i], nums[i]+dp[i-1]) |
| [918. 环形子数组的最大和](https://leetcode.cn/problems/maximum-sum-circular-subarray/description)| 中等+ | dp[i] = max(nums[i], nums[i]+dp[i-1]), max(最大，总和-最小) |
| [121. 买卖股票的最佳时机](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/description)| 简单+ | dp |
| [122. 买卖股票的最佳时机 II](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/description)| 中等+ | dp |
|[123. 买卖股票的最佳时机 III](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/description)| 困难+ | dp |
|[188. 买卖股票的最佳时机 IV](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/description)| 困难+ | dp |



# 模板
## Kadane(最大子数组和)
```
        dp.push_back(nums[0]);
        for (int i = 1; i < nums.size(); i++) {
            int dpi = max(nums[i], nums[i] + dp[i - 1]);
            dp.push_back(dpi);
        }
```

## 买卖股票类问题统一模板
```
class Solution {
public:
    /**
     * 统一解法：最多进行 k 次完整交易（买入 + 卖出 = 1 次）
     * 
     * 核心思想：模拟一个股民的交易生涯
     * - sell[i]：已经成功完成了 i 次交易，当前手上没有股票，钱包里有多少钱？
     * - buy[i] ：已经成功完成了 i 次交易，但现在已经买入了下一股（准备第 i+1 次卖出），钱包里剩多少钱？
     * 
     * 注意：交易次数 i 的范围是 0 到 k
     *   - sell[0] = 0（没交易过，也没赚钱）
     *   - buy[0] 不需要显式维护（因为第一次买入来自 sell[0]）
     */
    int maxProfit(int k, vector<int>& prices) {
        // 初始化状态数组
        // buy[i] 初始为负无穷：表示初始无法持有股票
        // sell[i] 初始为 0：表示未交易时利润为 0
        vector<int> buy(k + 1, INT_MIN);
        vector<int> sell(k + 1, 0);

        // 遍历每一天的股价
        for (int price : prices) {
            // 尝试更新完成 1 到 k 次交易的状态
            for (int i = 1; i <= k; ++i) {
                // 📥 更新 buy[i]：
                // “我已经完成了 i 次交易，现在又买了一股” 的钱怎么来？
                //   - 要么我之前就处于这个状态（buy[i] 不变）
                //   - 要么我之前完成了 i-1 次交易并且空仓（sell[i-1]），现在用那些钱买入 → sell[i-1] - price
                buy[i] = max(buy[i], sell[i - 1] - price);

                // 💰 更新 sell[i]：
                // “我已经完成了 i 次交易，现在空仓” 的钱怎么来？
                //   - 要么我一直空仓（sell[i] 不变）
                //   - 要么我之前完成了 i 次交易但还持股（buy[i]），现在把它卖掉 → buy[i] + price
                sell[i] = max(sell[i], buy[i] + price);
            }
        }

        // 🏁 最终目标：完成最多 k 次交易，并且空仓离场
        return sell[k];
    }

    // LeetCode 123：最多交易 2 次
    int maxProfit(vector<int>& prices) {
        return maxProfit(2, prices);
    }
};
```
