'''
username = input("请输入用户名：")
password = input("请输入密码：")

if username.lower().strip() == "admin" and password == "123.com":
    print("登陆成功！")
else:
    print("用户名或密码错误！")

#   lower() --- 把字符串转给小写
#   upper() --- 把字符串转为大写
'''
#
chinese_score = int(input("请输入语文成绩："))
maths_score = int(input("请输入数学成绩："))
english_score = int(input("请输入英语成绩："))

get_course = ""

if chinese_score>=60 and maths_score>=60 and english_score>=60:
    print("恭喜你，所有科目都通过了考试了！")
else:
    if chinese_score<60: get_course="语文 "
    if maths_score<60:  get_course+="数学 "
    if english_score<60:    get_course+="英语 "
    print("很遗憾，你没有通过全部考试，需要补考的科目为：" + get_course)
 

