# Creatinine Clearance Calculator
# IBI1 Practical - Creatinine Clearance Exercise

# ============================================
# 伪代码 (Pseudocode)
# ============================================
"""
1. 获取用户输入：年龄、体重、性别、肌酐浓度
2. 检查输入值是否在有效范围内：
   - 年龄 < 100
   - 体重在 20-80kg 之间
   - 肌酐浓度 > 0
3. 根据性别选择相应的计算公式常数
   - 男性: 无调整系数
   - 女性: × 0.85
4. 应用 Cockcroft-Gault 方程计算 CrCl
   CrCl = (140 - 年龄) × 体重 × (0.85 if 女性) / 肌酐浓度
5. 输出计算结果
6. 如果输入无效，应报错提示
"""

# ============================================
# 6.2 方程与实现 (Implementation)
# ============================================

def calculate_creatinine_clearance(age, weight, gender, creatinine):
    """
    根据 Cockcroft-Gault 方程计算肌酐清除率 (CrCl)
    
    参数:
        age: 年龄 (岁)
        weight: 体重 (kg)
        gender: 性别 ("male" 或 "female")
        creatinine: 肌酐浓度 (μmol/L)
    
    返回:
        CrCl 值 (mL/min)
    """
    
    # 输入验证 - 检查年龄
    if age <= 0 or age >= 100:
        return None, "错误: 年龄必须在 1-99 岁之间"
    
    # 输入验证 - 检查体重
    if weight < 20 or weight > 80:
        return None, "错误: 体重必须在 20-80 kg 之间"
    
    # 输入验证 - 检查肌酐浓度
    if creatinine <= 0:
        return None, "错误: 肌酐浓度必须大于 0"
    
    # 输入验证 - 检查性别
    gender = gender.lower()
    if gender not in ["male", "female", "m", "f"]:
        return None, "错误: 性别必须是 'male' 或 'female'"
    
    # 计算 Cockcroft-Gault 方程
    # CrCl = (140 - age) × weight × factor / creatinine
    if gender in ["female", "f"]:
        factor = 0.85  # 女性需要乘以 0.85
    else:
        factor = 1.0  # 男性不需要调整
    
    crcl = ((140 - age) * weight * factor) / creatinine
    
    return crcl, None


# 主程序 - 获取用户输入并计算
if __name__ == "__main__":
    print("=" * 50)
    print("肌酐清除率 (CrCl) 计算器")
    print("Cockcroft-Gault 方程")
    print("=" * 50)
    
    try:
        # 获取用户输入
        age = float(input("请输入年龄 (岁): "))
        weight = float(input("请输入体重 (kg): "))
        gender = input("请输入性别 (male/female): ")
        creatinine = float(input("请输入肌酐浓度 (μmol/L): "))
        
        # 计算 CrCl
        crcl, error_message = calculate_creatinine_clearance(age, weight, gender, creatinine)
        
        if error_message:
            # 如果有错误，输出错误信息
            print(f"\n{error_message}")
        else:
            # 输出计算结果
            print(f"\n计算结果:")
            print(f"CrCl = {crcl:.2f} mL/min")
            
            # 提供参考解读
            if crcl >= 90:
                print("解读: 肾功能正常")
            elif crcl >= 60:
                print("解读: 肾功能轻度下降")
            elif crcl >= 30:
                print("解读: 肾功能中度下降")
            else:
                print("解读: 肾功能严重下降")
    
    except ValueError:
        print("\n错误: 请输入有效的数字")
