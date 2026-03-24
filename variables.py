# Variables and Population Growth Analysis
# IBI1 Practical - Variables Exercise

# ============================================
# 4.1 Some simple math
# ============================================

# 4.1.1 存储不同年份的人口数据
a = 5.08      # 2004年苏格兰估算人口 (百万)
b = 5.33      # 2014年苏格兰估算人口 (百万)
c = 5.55      # 2024年苏格兰估算人口 (百万)

# 4.1.2 计算相邻10年的人口变化量
d = b - a     # 2004-2014年人口变化
e = c - b     # 2014-2024年人口变化

# 4.1.3 比较变化量并判断趋势
# Is population growth accelerating or decelerating in Scotland?
if e > d:
    print("Population growth is accelerating")
    # 2014-2024年的变化量(0.22)大于2004-2014年的变化量(0.25)
    # 等等，0.25 > 0.22，所以是 decelerating (减速)
else:
    print("Population growth is decelerating")
    # 2014-2024年的变化量(0.22)小于2004-2014年的变化量(0.25)
    # 人口增长减速

print(f"2004-2014年人口变化 (d): {d} 百万")
print(f"2014-2024年人口变化 (e): {e} 百万")

# ============================================
# 4.2 Booleans
# ============================================

# 创建布尔变量
X = True
Y = False

# 创建新变量 W = X or Y
W = X or Y

# ============================================
# 布尔值真值表 (Truth Table for W = X or Y)
# ============================================
# X=True, Y=False => W=True
# X=True, Y=True  => W=True
# X=False, Y=False => W=False
# X=False, Y=True => W=True
