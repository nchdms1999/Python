# break跳出整个循环，continue跳出当前循环
'''
print("====== break测试 ======")
num = 10
i = 0
while i <= num:
    i += 1
    if i == 5: break
    else:
        print(i, end=" ")
else: print("===== break测试结束 =====")

print("\n====== continue测试 ======")
num = 10
i = 0
while i <= num:
    i += 1
    if i == 5: continue
    else:
        print(i, end=" ")
else: print("\n===== continue测试结束 =====")
'''
# 2006年学校80000人，每年增长25%，请问按此增长数据，到哪年学生人数达到20万人
stu_num = 80000
years = 0
while True: # 不强制跳出，即一直循环
    stu_num *= 1.25
    years += 1
    if stu_num > 200000: break
print("到%d年后学生人数到20万" % (years+2006))
