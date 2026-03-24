# Infection Spread Simulation
# IBI1 Practical - Infection Exercise

# ============================================
# 5.1 定义初始参数
# ============================================

total_students = 91         # 班级总人数 (N=91)
initial_infected = 5        # 初始感染人数
growth_rate = 0.40          # 感染增长率 (40%)
days = 0                    # 初始天数

# ============================================
# 5.2 初始化感染人数
# ============================================
current_infected = initial_infected

# ============================================
# 5.3 循环计算每天的感染人数
# ============================================
print("天数\t累计感染人数")
print("-" * 25)

# 循环直到感染人数超过班级总人数
while current_infected < total_students:
    days += 1
    # 计算新增感染人数并累加到当前总感染人数
    # 每天的增长 = 当前感染人数 × 增长率
    current_infected += current_infected * growth_rate
    
    # 输出当天数据，使用 int() 取整
    print(f"{days}\t{int(current_infected)}")

# 输出最终结果
print("-" * 25)
print(f"全班{total_students}人感染共需 {days} 天")
print(f"最终感染人数: {int(current_infected)} 人")