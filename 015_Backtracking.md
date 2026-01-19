

# 练习

| 题目名称                                      | 难度   |思路|
|---------------------------------------------|--------|---|
| [17. 电话号码的字母组合](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/description)| 中等 | umap + combination |
| []()| 中等 | 1 |
| [79. 单词搜索](https://leetcode.cn/problems/word-search/description)| 中等 | DFS + 回溯 + 剪枝 |

# 模板
## umap初始化 + 组合模板
```
    std::unordered_map<int, std::vector<std::string>> umap = {
        {2, {"a", "b", "c"}}, {3, {"d", "e", "f"}},
        {4, {"g", "h", "i"}}, {5, {"j", "k", "l"}},
        {6, {"m", "n", "o"}}, {7, {"p", "q", "r", "s"}},
        {8, {"t", "u", "v"}}, {9, {"w", "x", "y", "z"}}};

    void dfs(string& digits, int idx, string& current,
             vector<string>& dst) {
        if (idx == digits.length()) {
            // cout << current << endl;
            dst.push_back(current);
            return;
        }
        int pos = digits[idx] - '0';
        for (auto itr : umap[pos]) {
            current += itr;
            dfs(digits, idx + 1, current, dst);
            current.pop_back();
        }
    }
```

## DFS + 回溯
```
                // 标记为已访问
                visited[tmpr][tmpc] = true;

                // 递归搜索下一个字符
                dfs(tmpr, tmpc, word, idx + 1, board, visited, ret);

                // 【回溯】关键！恢复 visited 状态，以便其他路径使用
                visited[tmpr][tmpc] = false;
```
