#num01 = input("请输入第一个数：")
#num02 = input("请输入第二个数：")
#print(type(num01))
# 需要把字符串类型转换为整形
#print("%d + %d = %d" %(int(num01),int(num02),int(num01)+int(num02)))

# 总结
"""
    数据类型转换：要转换的类型（数据）
    1. 要把num01转为整数     int(num01)
    2. 转为浮点数           float()
    3. 转为字符串           str()
    4. 转为布尔类型         bool()
"""
print(int("12345")+1)
print(float("12.345")+1.187)
print(str(123)+"456")
print(bool(1))

print(int(12.945))  #去除小数点后的值
# 数据类型转换，不是所有转换都能成功，需做异常处理

# 数值--字符
print(ord("x"))
print(chr(88))

# 进制
