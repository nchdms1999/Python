'''
# 输入一个正数，求出从1到此数所有包含3及3的倍数之和。
num = int(input("请输入一个正整数："))

i = 1
sum = 0

while i <= num:
    if i % 3 == 0:
        sum += i
    elif "3" in str(i):
        sum += i
    else: pass  # 此行可省略
    i += 1
print("从1到此数%d所有包含3的数字及3的倍数之和为：%d" % (num,sum))
'''
'''
# 输入班级人数，然后依次输入所有学员的成绩，计算改该班学员的平均成绩和总成绩。
a = int(input("请输入该班学生人数："))

i = 1
total = 0

while i <= a:
    score = int(input("请输入第%d个学生成绩：" % i))
    total += score
    i += 1
print("该班级学员平均成绩为：%d，总分为：%d" % (total/a,total))
'''

# 输入正整数n，求出n与其反序数之和。
num = input("请输入一个正整数：")

i = 0
new_num = ""

while i < len(num): # len()函数可直接取数字位数（作为字符时），一个python语言的优点！
    new_num = num[i] +new_num   # 原数字从前往后取位数赋予新数
    i += 1
else: print("循环结束！")   # 当循环条件为False时执行的语句
print("%s+%s=%d" % (num,new_num,int(num)+int(new_num)))
