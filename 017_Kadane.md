

# 练习

| 题目名称                                      | 难度   |思路|
|---------------------------------------------|--------|---|
| [53. 最大子数组和](https://leetcode.cn/problems/maximum-subarray/description)| 中等+ | dp[i] = max(nums[i], nums[i]+dp[i-1]) |
| [918. 环形子数组的最大和](https://leetcode.cn/problems/maximum-sum-circular-subarray/description)| 中等+ | dp[i] = max(nums[i], nums[i]+dp[i-1]), max(最大，总和-最小) |
| [121. 买卖股票的最佳时机](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/description)| 简单+ | mini = min(mini, prices[i]) , maxi = max(maxi, prices[i]-mini) |
| [122. 买卖股票的最佳时机 II](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/description)| 中等+ | dp |
|[]()| 中等+ | dp |
|[]()| 中等+ | dp |



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
```
