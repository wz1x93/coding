
# 练习

| 题目名称                                      | 难度   |思路|
|---------------------------------------------|--------|---|
| [909. 蛇梯棋](https://leetcode.cn/problems/snakes-and-ladders/description) | 中等+ | BFS + queue<pair<pos,step>> |
| [433. 最小基因变化](https://leetcode.cn/problems/minimum-genetic-mutation/description) | 中等+ | DFS + set.insert |
| [127. 单词接龙](https://leetcode.cn/problems/word-ladder/description) | 困难+ | BFS + unordered_set<new word> + unordered_map<pair<word, step>> |
| []() | 简单 |  |


# 模板
## 获取所有节点
```
        // 将vector转成unordered_set，提高查询速度
        unordered_set<string> wordSet(wordList.begin(), wordList.end());

        // 记录word是否访问过
        unordered_map<string, int> visitMap; // <word, 查询到这个word路径长度>
```
