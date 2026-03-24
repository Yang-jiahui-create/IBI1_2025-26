# Infection Spread Simulation
# IBI1 Practical - Infection Exercise

# ============================================
# Pseudocode / 伪代码
# ============================================
"""
1. Set total number of students N=91
2. Set initial infected students = 5
3. Set growth rate = 40%
4. For each day:
   - Calculate new infections = current_infected * growth_rate
   - Add to current infected
   - Stop when current_infected >= 91
5. Display number of infected each day and total days
"""

# ============================================
# 5 Simulating Infection Rates Over Time
# ============================================

# 初始参数
total_students = 91         # 班级总人数
initial_infected = 5        # 初始感染人数
growth_rate = 0.40          # 增长率 40%

# 初始化
current_infected = initial_infected
days = 0

# 输出表头
print("Day\tInfected")

# 循环计算每天的感染人数
while current_infected < total_students:
    days = days + 1
    current_infected = current_infected + (current_infected * growth_rate)
    print(f"{days}\t{int(current_infected)}")

# 报告感染全班所需天数
print(f"Total days to infect all: {days}")
