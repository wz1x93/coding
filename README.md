# coding
- 20260219 1 + 11 + 128
- 20260221 15 + 42 + 283 
- 20260224 3 + 438 + !76
- 20260302 !560[前缀和] + !239[priority_queue<pair<int, int>>] + 73
- 20260303 54 + ?!41 + !238[上下三角]
- 20260308 !46 +78 +17
- 20260309 29+22+!94 std::find std::min_element stk.empty() return 0
- 20260312 102 + 104 + !98 dfs(TreeNode* root, long long lower, long long upper) {
- 20260314 48 + 240 + !74  lower_bound it_low != matrix[i].end() && *it_low == target
- 20260315 34 + !153 + 33 先做153明确二分寻找最小值代码，然后33寻找最小值从两段二分找target
- 20260316 230 + 199 + 35
- 20260317 200 + !739 + 70 先进栈，出现大值不停出栈，记位置差
- 20260318 994 + 56 + 21
- 20260320 19 + 24 + 114 void flatten(TreeNode* root) 不能直接赋值：root = new_node 在 void 函数中对外部无效
- 20260321 148 + 142 + 136 找环(快慢指针确认环+快慢指针二次寻找位置)， 全员异或运算(ret ^= nums[i])可以使得出现两次的变为0一次的显示
- 20260322 207 + 20 + 155 使用map统计dst对应的所有src，in_degree统计dst的边个数，找到入度为0的节点，BFS持续删除入度，最终确认in_degree是否都为0
- 20260323 !208 + 347 + !101 前缀树构建字母多叉树，对称二叉树，左右都空回true，单左单右左右不等回false，回左左右右&&左右右左
- 20260324 215 + !295 + 118  左等右（右推，左推右顶，右出顶），else（左推，右推左顶，左出顶）
- 20260326 !394 + !2 + 169 stack<pair<int, string>> stk , int x = l1 != nullptr ? l1->val : 0 ，int sum = x + y + carry
- 20260327 189 + 25 + !543 某个节点开始左右延伸最远加和为最长（不是根节点）
- 20260329 !55 + !45 + 121 1) farthest = max(farthest, i + nums[i]);  2) st = ed, ed = farthest+1
- 20260330 198 + 79 + !141 快慢指针，快的先到NULL返回false，否则两个相遇
- 20260401 !287 + 226 + !152 快慢指针，维护最大最小两个值的DP处理
- 20260402 199 + 1161 + 872

leetcode精选100完成后可以考虑刷这个
https://github.com/EndlessCheng/codeforces-go/blob/master/leetcode/SOLUTIONS.md
