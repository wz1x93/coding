
# 练习

| 题目名称                                      | 难度   |思路|
|---------------------------------------------|--------|---|
| [70. 爬楼梯](https://leetcode.cn/problems/climbing-stairs/description) | 简单 | dp[i]=dp[i-1]+dp[i-2] |
| [198. 打家劫舍](https://leetcode.cn/problems/house-robber/description) | 中等+ | dp[i]=max(dp[i-1], dp[i-2]+nums[i]) |
| [300. 最长递增子序列](https://leetcode.cn/problems/longest-increasing-subsequence/description) | 中等+ | i为末的最长递增子序列，dp[i]=max(dp[i],dp[j]+1) |
| []() | 简单 |  |


# 模板
## 获取所有节点
```
