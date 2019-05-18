"""
print(100 +200)
print(100 - 200)
print(100 * 200)
print(round(10 / 3, 2))
print("%.2f" % (10/3))
print("{:.2f}" .format(10/3))
print(10//3)    # 取整
print(10 % 3)   # 取余数
print(3**4)     # 幂
"""

"""
num = int(input("请输入一个三位数："))
hundred = num // 100
den = num % 100 // 10 
unit = num % 10

print("三位数{0}的百位数字：{1} 十位数字：{2} 个位数字：{3}" .format(num,hundred,den,unit))
"""

num = input("请输入一个三位数：")
print("三位数{0}的百位数字：{1} 十位数字：{2} 个位数字：{3}" .format(num,num[0],num[1],num[2]))
