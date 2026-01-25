# 练习

| 题目名称                                      | 难度   |思路|
|---------------------------------------------|--------|---|
| [242. 有效的字母异位词](https://leetcode.cn/problems/valid-anagram/description)| 简单 | unordered_map<char, int> |
| [49. 字母异位词分组](https://leetcode.cn/problems/group-anagrams/description)| 中等 |  |
| []()| 中等 |  |
| []()| 中等+ |  |

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
