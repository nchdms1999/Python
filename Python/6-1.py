#
num = int(input("请输入一个整数，以便算出1到此数的累计和："))

i = 1
sum = 0

while i <= num:
    sum += i
    i += 1
print("从1累加到%d的和为：%d" %(num,sum))
