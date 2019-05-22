# 先输入一个年份，再输入一个月份，输出该月天数。


# 涨工资规则：<=4000涨20%；4k-6k涨15%；6k-8k涨10%；8k-12k涨5%；>12k涨500。
# 输入一个工资金额，输出涨工资后的金额。
'''
salary = float(input("请输入该员工现在的工资："))

s1 = salary * 1.2
s2 = salary * 1.15
s3 = salary * 1.1
s4 = salary * 1.05
s5 = salary + 500

if salary <= 4000:
    print("该员工调整后的工资为：%.2f元。" % s1)
elif salary > 4000 and salary <= 6000:
    print("该员工调整后的工资为：%.2f元。" % s2)
elif salary > 6000 and salary <= 8000:
    print("该员工调整后的工资为：%.2f元。" % s3)
elif salary > 8000 and salary <= 12000:
    print("该员工调整后的工资为：%.2f元。" % s4)
else:
    print("该员工调整后的工资为：%.2f元。" % s5)
'''
# 实现一个简单的计算器
'''
num01 = float(input("请输入第一个数："))
operator = input("请选择要执行的操作【+，-，*，/，%】：")
num02 = float(input("请输入第二个数："))

add = num01 + num02
min = num01 - num02
mul = num01 * num02
div = num01 / num02
mod = num01 % num02

if operator=="+":
    print("计算结果：%.2f" % add)
elif operator=="-":
    print("计算结果：%.2f" % min)
elif operator=="*":
    print("计算结果：%.2f" % mul)
elif operator=="/":
    print("计算结果：%.2f" % div)
elif operator=="%":
    print("计算结果：%.2f" % mod)
else:
    print("所属运算符不合法！")
'''