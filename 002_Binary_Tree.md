# 练习

| 题目名称                                      | 难度   |思路|
|---------------------------------------------|--------|---|
| [104. 二叉树的最大深度](https://leetcode.cn/problems/maximum-depth-of-binary-tree/description) | 简单 |  |
| [100. 相同的树](https://leetcode.cn/problems/same-tree/description) | 简单 ||
| 翻转二叉树                                   | 简单   ||
| 对称二叉树                                   | 简单   ||
| 从前序与中序遍历序列构造二叉树               | 中等   ||
| 从中序与后序遍历序列构造二叉树               | 中等   ||
| 填充每个节点的下一个右侧节点指针 II          | 中等   ||
| 二叉树展开为链表                             | 中等   ||
| 路径总和                                     | 简单   ||
| 求根节点到叶节点数字之和                     | 中等   ||
| [124. 二叉树中的最大路径和](https://leetcode.cn/problems/binary-tree-maximum-path-sum/description)          | 困难 ||
| 二叉搜索树迭代器                             | 中等   ||
| [222. 完全二叉树的节点个数](https://leetcode.cn/problems/count-complete-tree-nodes/description)             | 简单 ||
| [236. 二叉树的最近公共祖](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/description) | 中等 ||

# 模板
## 获取所有节点
```
void getallnodes(TreeNode* root, vector<TreeNode*>& allnodes) {
        queue<TreeNode*> que;
        que.push(root);

        while (!que.empty()) {
            TreeNode* tmp = que.front();
            que.pop();

            if (tmp->left) {
                que.push(tmp->left);
            }
            if (tmp->right) {
                que.push(tmp->right);
            }
            allnodes.push_back(tmp);
        }
    }
```
