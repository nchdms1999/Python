
import sys

str01 = input("请输入任意一段字符：")
print("str01的数据类型：", type(str01))

num01 = input("请输入任意一个数字：")
print("num01占用的空间为：", sys.getsizeof(num01))

num01 = int(input("请输入任意一个数字："))
print("num01占用的空间为：", sys.getsizeof(num01))

num01 = 123
print("num01占用的空间为：", sys.getsizeof(num01))

