"""
total = 145893
day = total // (24 * 60 * 60)
hour = (total % (24*60*60)) // (60*60)
minute = (total % (60*60)) // 60
second = total % 60

print("%d秒为 %d天 %d小时 %d分 %d秒" % (total,day,hour,minute,second))
"""

chinese = int(input("请输入语文分数："))
maths = int(input("请输入数学分数："))
english = int(input("请输入英语分数："))

total = chinese + maths + english 
average = total / 3

print("本次考试的总分：%.2f，平均分：%.2f" % (total,average))




