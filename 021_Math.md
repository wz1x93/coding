# 练习

| 题目名称                                      | 难度   |思路|
|---------------------------------------------|--------|---|
| []()| 中等+ | 1 |
| [201. 数字范围按位与](https://leetcode.cn/problems/bitwise-and-of-numbers-range/description)| 中等+ | 二进制公共前缀 + 移位操作 |

# 模板
## 二进制公共前缀
```
        int shift = 0;
        while(left != right){
            left >>= 1;
            right >>= 1;
            shift++;
        }
        return left <<= shift;

```
