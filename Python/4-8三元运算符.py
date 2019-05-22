# 又称为条件表达式, 条件选择的一种简单写法: a if 1 else b
'''
num01 = 100 if 100>200 else 200
print(num01)

if 100>200:
    num01 = 100
else:   num01 = 200

print(num01)   
'''
'''
username = input("请输入用户名：")
password = input("请输入密码：")
result = "登陆成功！" if username == "Admin" and password == "123.com" else "用户名或密码错误！"
print(result)
'''
num01, num02 = eval(input("输入两个不相等的数，以逗号分割："))
print("num01大于num02!" if num01>num02 else "num01小于num02!")

