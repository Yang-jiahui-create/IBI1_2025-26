# Creatinine Clearance Calculator
# IBI1 Practical - Creatinine Clearance Exercise

# ============================================
# Pseudocode / 伪代码
# ============================================
"""
1. Get user input: age, weight, gender, creatine concentration (Cr)
2. Check input values are within correct ranges:
   - age < 100 years
   - weight > 20kg and < 80kg  
   - creatine concentration > 0 μmol/l and < 100 μmol/l
   - gender = male or female
3. If input is invalid, report error message about which variable needs correction
4. If input is valid, calculate CrCl using Cockcroft-Gault Equation:
   CrCl = (140 - age × weight) / (72 × Cr) × 0.85 (if female)
5. Output the CrCl value
"""

# ============================================
# 7 Creatine Clearance Calculator
# ============================================

# Cockcroft-Gault Equation: 
# CrCl = (140 - age × weight) / (72 × Cr) × 0.85 (if female)

def calculate_crcl(age, weight, gender, Cr):
    """
    Calculate Creatinine Clearance using Cockcroft-Gault Equation
    
    Parameters:
        age: age in years
        weight: weight in kg
        gender: "male" or "female"
        Cr: creatine concentration in μmol/l
    
    Returns:
        CrCl value or error message
    """
    
    # 输入验证 - Check input values are within correct ranges
    
    # Check age
    if age >= 100:
        return "Error: age needs corrected (must be < 100 years)"
    
    # Check weight
    if weight <= 20:
        return "Error: weight needs corrected (must be > 20kg)"
    if weight >= 80:
        return "Error: weight needs corrected (must be < 80kg)"
    
    # Check creatine concentration
    if Cr <= 0:
        return "Error: creatine concentration needs corrected (must be > 0 μmol/l)"
    if Cr >= 100:
        return "Error: creatine concentration needs corrected (must be < 100 μmol/l)"
    
    # Check gender
    gender = gender.lower()
    if gender not in ["male", "female"]:
        return "Error: gender needs corrected (must be 'male' or 'female')"
    
    # 计算 CrCl
    # CrCl = (140 - age × weight) / (72 × Cr) × 0.85 (if female)
    if gender == "female":
        crcl = (140 - age * weight) / (72 * Cr) * 0.85
    else:
        crcl = (140 - age * weight) / (72 * Cr)
    
    return crcl


# 主程序
# 使用 str() 转换数字为字符串进行输出
age = int(input("Enter age (years): "))
weight = float(input("Enter weight (kg): "))
gender = input("Enter gender (male/female): ")
Cr = float(input("Enter creatine concentration (μmol/l): "))

result = calculate_crcl(age, weight, gender, Cr)

# 输出结果
if isinstance(result, str):
    # 如果是错误信息
    print(result)
else:
    # 如果是计算结果
    print("CrCl = " + str(result) + " mL/min")
