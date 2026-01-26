

# 练习

| 题目名称                                      | 难度   |思路|
|---------------------------------------------|--------|---|
| [399. 除法求值](https://leetcode.cn/problems/evaluate-division/description)| 中等 | hashmap判断节点存在 + DFS |
| [207. 课程表](https://leetcode.cn/problems/course-schedule/description)| 中等+ | Kahn w/ BFS累加 |
| [210. 课程表 II](https://leetcode.cn/problems/course-schedule-ii/description)| 中等+ | Kahn w/ BFS记录 |
| []()| 中等+ | |

# 模板
## Kahn 算法 (A → B → C ← D ← E, 其中AE没有依赖关系，所以可以先修，之后才能修BD，而且BD也没有顺序问题)
```
        vector<vector<int>> graph;
        vector<int> indegree;

        graph.resize(numCourses);
        indegree.resize(numCourses, 0);

        vector<int> ret;

        for (int i = 0; i < prerequisites.size(); i++) {
            int pre = prerequisites[i][1];
            int pst = prerequisites[i][0];
            graph[pre].push_back(pst);
            indegree[pst]++;
        }

        queue<int> que;
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) {
                que.push(i);
                cout << i;
            }
        }

        while (!que.empty()) {
            int tmp = que.front();
            que.pop();
            ret.push_back(tmp);

            for (auto itr : graph[tmp]) {
                indegree[itr]--;
                if (indegree[itr] == 0) {
                    que.push(itr);
                }
            }
        }

        if (ret.size() == numCourses) {
            return ret;
        }
        return {};

```
