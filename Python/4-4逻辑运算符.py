"""
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print(not True)
print(not False)
"""
'''
username = input("请输入用户名：")
password = input("请输入密码：")

u = "Admin"
p = "123.com"

if (username == u and password == p) :
    print("登陆成功！")
else: print("用户名或密码错误！")
'''
'''
chinese = int(input("请输入语文分数："))
maths = int(input("请输入数学分数："))

print("老王的成绩是否都大于90分： ",(chinese>=90 and maths>=90))
print("老王的成绩是否有一门大于90分： ",(chinese>=90 or maths>=90))
'''
year = int(input("请输入一个年份，以判断是否为闰年："))

c1 = year % 400
c2 = year % 4 or (not(year % 100))

if c1 == 0 or c2 == 0:
    print("%d是闰年！" % year)
else: print("%d是平年！" % year)
