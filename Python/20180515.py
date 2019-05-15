name = "Alice"
gender = "男"
age = 23

print("姓名：{} 姓名：{} 年龄：{}" .format(name,gender,age))
print("姓名：{0} 姓名：{1} 年龄：{2} 学生姓名：{0}" .format(name,gender,age))
print("姓名：{name} 姓名：{gender} 年龄：{age} 学生姓名：{name}" .format(name=name,gender=gender,age=age))

print("姓名：{:10}" .format(name))
print("姓名：{:<10}" .format(name))
print("姓名：{:>10}" .format(name))
print("姓名：{:^10}" .format(name))

print("{:10.2f}" .format(3.1415926))#保留两位小数，10个占位符，默认对齐
print("{:<10.2f}" .format(3.1415926))
print("{:^10.2f}" .format(3.1415926))

# 数值操作
num01, num02 = 200, 300
print("十六进制打印：{0:x} {1:x}" .format(num01,num02))
print("八进制打印：{0:o} {1:o}" .format(num01,num02))
print("十进制打印：{0:d} {1:d}" .format(num01,num02))
print("二进制打印：{0:b} {1:b}" .format(num01,num02))

print("{:c}" .format(76))
print("{:e}" .format(123456.77544))
print("{:0.2e}" .format(123456.77544))
print("{:0.2g}" .format(123456.77544))
print("{:0.2%}" .format(34))

# 千位分隔符
print("{:,}" .format(1234567890))
