stunum = input("请输入学生学号：")
stuname = input("请输入学生姓名：")
c_score = input("请输入[学号：%s 姓名：%s] 语文成绩：" % (stunum,stuname))
m_score = input("请输入[学号：%s 姓名：%s] 数学成绩：" % (stunum,stuname))
f_score = input("请输入[学号：%s 姓名：%s] 外语成绩：" % (stunum,stuname))

total = float(c_score)+float(m_score)+float(f_score)
average = total/3

print("=================成绩统计===================")
print("学号：%s 姓名：%s" % (stunum,stuname))
print("总分：%.2f 均分：%.2f" % (total,average))
print("成绩明细[语文：%.2f  数学：%.2f  外语：%.2f]" % (float(c_score),float(m_score),float(f_score)))

