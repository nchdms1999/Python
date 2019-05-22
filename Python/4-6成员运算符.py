
# in ; not in
str01 = "my name is KK, I come from China"
if "come" in str01:
    print("include")
else:   print("not include")


name_array = ["Alice","Bob","Peter","Tomas"]
name = input("Please input name: ")
if name in name_array:
    print("The name %s is in the List!" % name)
else:   print("The name %s is NOT in the List" % name)

num_array = [10,20,30,40,50,60]
if 23 in  num_array:
    print("Exist!")
else:   print("NOT Exist!")

