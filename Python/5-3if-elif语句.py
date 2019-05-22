#
chinese_score = int(input("请输入语文成绩："))
maths_score = int(input("请输入数学成绩："))
english_score = int(input("请输入英语成绩："))

average = (chinese_score+maths_score+english_score)/3

if average>=90:
    print("A")
elif average>=80 and average<90:
    print("B")
elif average>=70 and average<80:
    print("C")
elif average>=60 and average<70:
    print("D")
else: print("E")
