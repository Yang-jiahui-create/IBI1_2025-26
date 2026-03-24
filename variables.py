# Variables and Population Growth Analysis
# IBI1 Practical - Variables Exercise

# ============================================
# 4.1 人口变化计算 (Population Change)
# ============================================

# 4.1.1 存储不同年份的人口数据 (百万)
population_2004 = 5.08   # 2004年估算人口
population_2014 = 5.33   # 2014年估算人口
population_2024 = 5.55   # 2024年估算人口

# 4.1.2 计算相邻10年的人口变化量
change_2004_2014 = population_2014 - population_2004
change_2014_2024 = population_2024 - population_2014

# 4.1.3 比较变化量并判断趋势
# 如果 2014-2024年的变化量 > 2004-2014年的变化量，则增长加速
if change_2014_2024 > change_2004_2014:
    growth_trend = "accelerating"  # 增长加速
else:
    growth_trend = "decelerating"  # 增长减速

print(f"2004-2014年人口变化: {change_2004_2014} 百万")
print(f"2014-2024年人口变化: {change_2014_2024} 百万")
print(f"苏格兰人口增长趋势: {growth_trend}")

# ============================================
# 4.2 布尔值 (Boolean)
# ============================================

# 4.2.1 创建布尔变量
X = True    # 变量 X 为真
Y = False   # 变量 Y 为假

# 4.2.2 逻辑运算 - 使用 "or" 运算符
W = X or Y  # 只要 X 或 Y 中有一个为真，结果即为真

# 4.2.3 输出 W 的真值表结果
print(f"\nX = {X}")
print(f"Y = {Y}")
print(f"X or Y 的结果是: {W}")

# ============================================
# 真值表 (Truth Table)
# ============================================
print("\n真值表 (Truth Table):")
print("X     | Y     | X or Y")
print("-" * 25)

# 测试所有组合
test_cases = [(True, True), (True, False), (False, True), (False, False)]

for X_val, Y_val in test_cases:
    result = X_val or Y_val
    print(f"{str(X_val):5} | {str(Y_val):5} | {str(result):5}")
