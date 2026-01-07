# 练习

| 题目名称                                      | 难度   |思路|
|---------------------------------------------|--------|---|
| [108. 将有序数组转换为二叉搜索树](https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/description) | 简单+ | 中序重建二叉树 + vector<int>拆分 |
| [148. 排序链表](https://leetcode.cn/problems/sort-list/description) | 中等 | 遍历vector + 重构ListNode |
| [427. 建立四叉树](https://leetcode.cn/problems/construct-quad-tree/description) | 中等+  | 判断全1/全0 + DFS处理Node(grid, tl,tr,bl,br) |
| []() | 简单 | BFS |

# 模板
## 中序重建二叉树 + vector<int>拆分
```
    TreeNode* setup_tree(vector<int>& nums) {
        if (!nums.size()) {
            return nullptr;
        }
        int mid = nums.size() / 2;
        auto itr = std::find(nums.begin(), nums.end(), nums[mid]);
        int leftsize = std::distance(nums.begin(), itr);

        vector<int> vl(nums.begin(), itr);
        vector<int> vr(itr + 1, nums.end());

        TreeNode* left = setup_tree(vl);
        TreeNode* right = setup_tree(vr);
        return new TreeNode(nums[mid], left, right);
    }
```
