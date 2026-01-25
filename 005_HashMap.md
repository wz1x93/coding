# 练习

| 题目名称                                      | 难度   |思路|
|---------------------------------------------|--------|---|
| [242. 有效的字母异位词](https://leetcode.cn/problems/valid-anagram/description)| 简单 | unordered_map<char, int> |
| [49. 字母异位词分组](https://leetcode.cn/problems/group-anagrams/description)| 中等 | unordered_map<string, vector<string>> + sort() |
| [128. 最长连续序列](https://leetcode.cn/problems/longest-consecutive-sequence/description)| 中等 | unordered_map<int, int> 过滤 + 寻找连续 |
| []()| 中等+ |  |

# 模板
## 字母异位词分组
```
        unordered_map<string, vector<string>> mp;
        for (auto& s : strs) {
            string t = s;
            sort(t.begin(), t.end());
            mp[t].push_back(s);
        }
        vector<vector<string>> ans;
        for (auto& p : mp)
            ans.push_back(move(p.second));
        return ans;
```
