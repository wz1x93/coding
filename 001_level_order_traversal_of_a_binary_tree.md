'''
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
        // 最终结果：每一层最右边节点的值
        vector<int> ret;
        // 用于保存二叉树按层分组的所有节点值（可选，便于调试）
        vector<vector<int>> dst;

        // 边界条件：空树直接返回空结果
        if (!root) {
            return ret;
        }

        // 使用队列实现广度优先搜索（BFS / 层次遍历）
        queue<TreeNode*> que;
        que.push(root); // 从根节点开始

        // 当队列不为空时，继续处理每一层
        while (!que.empty()) {
            // 当前层的节点数量（关键！用于控制只处理当前层）
            int levelSize = que.size();
            // 存储当前层所有节点的值
            vector<int> cur;

            // 遍历当前层的所有节点（共 levelSize 个）
            for (int i = 0; i < levelSize; i++) {
                // 取出队列头部节点
                TreeNode* tmp = que.front();
                que.pop();

                // 将当前节点的子节点加入队列（为下一层做准备）
                if (tmp->left) {
                    que.push(tmp->left);
                }
                if (tmp->right) {
                    que.push(tmp->right);
                }

                // 记录当前节点的值到当前层列表
                cur.push_back(tmp->val);
            }

            // 将当前层的结果保存到 dst（用于后续取最右值，也可直接优化掉）
            dst.push_back(cur);
        }

        // 调试输出：打印每一层的节点值（可删除）
        for (auto itri : dst) {
            for (auto itrj : itri) {
                cout << itrj << ",";
            }
            cout << endl;
            // 每一层的最后一个元素就是从右侧看到的节点
            ret.push_back(itri.back());
        }

        return ret;
    }
};
'''
