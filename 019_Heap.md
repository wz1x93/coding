
# 练习

| 题目名称                                      | 难度   |思路|
|---------------------------------------------|--------|---|
| [373. 查找和最小的 K 对数字](https://leetcode.cn/problems/find-k-pairs-with-smallest-sums/description)| 中等+ | {sum,{nums1,nums2}} + 大顶堆 + 小于顶入堆 |
| [502. IPO](https://leetcode.cn/problems/ipo/description)| 困难+ | 排序{capital, profit} + 小于成本所有备选项入堆 |
| [295. 数据流的中位数](https://leetcode.cn/problems/find-median-from-data-stream/description)| 困难 | 大顶堆存小半，小顶堆存大半 + 大顶size=小顶size+1 + 均衡两堆个数 |

# 模板
## 大顶堆（默认）
```
// 小顶堆：堆顶是最小元素
std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap;

// 示例用法
minHeap.push(3);
minHeap.push(1);
minHeap.push(2);

std::cout << minHeap.top(); // 输出 1
minHeap.pop();              // 移除 1
```
