# 计算圆的周长和面积，pai取3.1415926，半径提示不能负数或者零，结果保留两位小数
r = float(input("请输入所求圆的半径："))
if r <= 0:

    print("半径值不能为负数或零，请重新输入！")
    
else:
    
    pai = 3.1415926
    c = 2 * pai * r
    s = pai * r * r

    print("圆的周长为： %.2f" %float(c))
    print("圆的面积为： %.2f" %float(s))



