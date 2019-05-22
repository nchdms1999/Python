#

chinese_score = int(input("请输入语文成绩："))
maths_score = int(input("请输入数学成绩："))
english_score = int(input("请输入英语成绩："))
'''
average = (chinese_score+maths_score+english_score)/3
# 使用条件选择
if average >= 90:
    print("你的平均分：%.2f，你真是个聪明的孩子！" % average)
if average < 60:
    print("你的平均分：%.2f，你要好好努力了！" % average)
# if语句一定要注意缩进
'''
get_course = ""

if (chinese_score==100 or maths_score==100 or english_score==100):
    if(chinese_score==100): get_course += "语文,"
    if(maths_score==100): get_course += "数学,"
    if(english_score==100): get_course += "英语"
    print("你的%s得了100分，奖励一朵小红花！" % get_course)
if (chinese_score>=90 and maths_score>=90) or (chinese_score>=90 and english_score>=90) or (maths_score>=90 and english_score>=90):
    if(chinese_score>=90): get_course += "语文,"
    if(maths_score>=90): get_course += "数学,"
    if(english_score>=90): get_course += "英语"
    print("你的%s大于90分，奖励一朵小红花！" % get_course)
if (chinese_score>=80 and maths_score>=80 and english_score>=80):
    print("你的语文，数学，英语都大于80分，奖励一朵小红花！")




