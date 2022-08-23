str1 = ' 123.242 '
# print(int(str1))
print(float(str1))

pi = 31.4159265
print ("%.4e" % (pi))

day = 14
month = 2
year = 2012

print("%d.%02d.%d" % (day, month, year))
# 14.02.2012
print("%d-%02d-%d" % (year, month, day))
# 2012-02-14
print("%d/%d/%d" % (year, day, month))