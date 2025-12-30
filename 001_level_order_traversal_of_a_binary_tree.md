```
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        // 最终结果：存储每层最右边节点的值
        vector<int> ret;
        // 可选：保存整棵树按层分组的节点值（便于调试）
        vector<vector<int>> dst;

        // 边界条件：空树直接返回空结果
        if (!root) {
            return ret;
        }

        // 使用队列实现 BFS（层次遍历）
        queue<TreeNode*> que;
        que.push(root); // 从根节点开始

        // 当队列不为空时，继续处理每一层
        while (!que.empty()) {
            // 当前层的节点数量（关键！用于限定只处理当前层）
            int levelSize = que.size();
            vector<int> cur; // 存储当前层所有节点的值

            // 遍历当前层的所有节点
            for (int i = 0; i < levelSize; i++) {
                TreeNode* tmp = que.front();
                que.pop();

                // 将子节点加入队列（为下一层做准备）
                if (tmp->left) {
                    que.push(tmp->left);
                }
                if (tmp->right) {
                    que.push(tmp->right);
                }

                // 记录当前节点值
                cur.push_back(tmp->val);
            }

            // 保存当前层结果
            dst.push_back(cur);
        }

        // 调试输出：打印每一层的节点（可删除）
        for (auto itri : dst) {
            for (auto itrj : itri) {
                cout << itrj << ",";
            }
            cout << endl;
            // 每层最后一个元素即为右视图看到的节点
            ret.push_back(itri.back());
        }

        return ret;
    }
};
```
