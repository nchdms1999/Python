# 输入姓名，性别 并打印
"""
print("请输入姓名：", end = "")
name = input()
print("请输入性别：", end = "")
gender = input()
print("姓名：%s 性别：%s" % (name,gender))
"""

# 简化写法
"""
name = input("请输入姓名：")
gender = input("请输入性别：")
print("姓名：%s 性别：%s" % (name,gender))
"""

# 输入两个数，求两个数之和
"""
num01 = input("请输入第一个数：")
num02 = input("请输入第二个数：")
print("%d + %d = %d" %(int(num01),int(num02),int(num01)+int(num02)))
# 所有输入的字符，都会被系统当作String类型
"""

num01,num02 = eval(input("请输入两个数，以逗号分隔："))
print("%d + %d = %d" %(num01,num02,num01+num02))
# eval函数特点：1.只能一次输入多个整数，自动转弯int类型，不能数字符串（报错）。
