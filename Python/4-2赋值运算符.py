total = 145893
day = total // (24 * 60 * 60)
hour = (total % (24*60*60)) // (60*60)
minute = (total % (60*60)) // 60
second = total % 60

print("%d秒为 %d天 %d小时 %d分 %d秒" % (total,day,hour,minute,second))

