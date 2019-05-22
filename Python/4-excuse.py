'''
# 输入一个五位数，求所有位上的数值之和
num5 = input("请输入一个五位的整数：")

sum = int(num5[0])+int(num5[1])+int(num5[2])+int(num5[3])+int(num5[4])

print("此五位数所有位上的和为：%d" % sum)
'''
# 输入自己的生日（比如：1987-08-16），计算这天是当年第几天。


year, month, day = eval(input("请按照'xxxx,xx,xx'的格式（以逗号分隔）输入一个日期："))

y_c1 = year % 400
y_c2 = year % 4 or (not(year % 100))
y_c = y_c1 == 0 or y_c2 == 0
month = int(month)
day = int(day)

if y_c:
    if month==1: 
        amount_day = day 
        print("所输日期是%d年第%d天！" % (year,amount_day))
    elif month==2: 
        amount_day = day+31 
        print("所输日期是%d年第%d天！" % (year,amount_day))
    elif month==3: 
        amount_day = day+60 
        print("所输日期是%d年第%d天！" % (year,amount_day))
    elif month==4: 
        amount_day = day+91 
        print("所输日期是%d年第%d天！" % (year,amount_day))
    elif month==5: 
        amount_day = day+121 
        print("所输日期是%d年第%d天！" % (year,amount_day))
    elif month==6: 
        amount_day = day+152 
        print("所输日期是%d年第%d天！" % (year,amount_day))
    elif month==7: 
        amount_day = day+182 
        print("所输日期是%d年第%d天！" % (year,amount_day))
    elif month==8: 
        amount_day = day+213 
        print("所输日期是%d年第%d天！" % (year,amount_day))
    elif month==9: 
        amount_day = day+244 
        print("所输日期是%d年第%d天！" % (year,amount_day))
    elif month==10: 
        amount_day = day+274 
        print("所输日期是%d年第%d天！" % (year,amount_day))
    elif month==11: 
        amount_day = day+305 
        print("所输日期是%d年第%d天！" % (year,amount_day))
    elif month==12: 
        amount_day = day+335 
        print("所输日期是%d年第%d天！" % (year,amount_day))   
    else:print("输入月份错误！")
else: 
    if month==1: 
        amount_day = day 
        print("所输日期是%d年第%d天！" % (year,amount_day))
    elif month==2: 
        amount_day = day+31 
        print("所输日期是%d年第%d天！" % (year,amount_day))
    elif month==3: 
        amount_day = day+59 
        print("所输日期是%d年第%d天！" % (year,amount_day))
    elif month==4: 
        amount_day = day+90 
        print("所输日期是%d年第%d天！" % (year,amount_day))
    elif month==5: 
        amount_day = day+120 
        print("所输日期是%d年第%d天！" % (year,amount_day))
    elif month==6: 
        amount_day = day+151 
        print("所输日期是%d年第%d天！" % (year,amount_day))
    elif month==7: 
        amount_day = day+181 
        print("所输日期是%d年第%d天！" % (year,amount_day))
    elif month==8: 
        amount_day = day+212 
        print("所输日期是%d年第%d天！" % (year,amount_day))
    elif month==9: 
        amount_day = day+243 
        print("所输日期是%d年第%d天！" % (year,amount_day))
    elif month==10: 
        amount_day = day+273 
        print("所输日期是%d年第%d天！" % (year,amount_day))
    elif month==11: 
        amount_day = day+304 
        print("所输日期是%d年第%d天！" % (year,amount_day))
    elif month==12: 
        amount_day = day+334 
        print("所输日期是%d年第%d天！" % (year,amount_day))   
    else:print("输入月份错误！") 

'''
# 输入5个100-200间的整数，打印出这5个数中的最大数和最小数。
import math
num01,num02,num03,num04,num05 = eval(input("请输入输入5个100-200间的整数，以逗号分隔："))

min5 = min(num01,num02,num03,num04,num05)
max5 = max(num01,num02,num03,num04,num05)

print("此5个数中，最大值为%d，最小值为%d。" % (max5,min5))
'''
