x = int(input("Enter total number of seconds  "))
y = x // 31536000 #y=years
rs = x % 31536000 #rs=remaining seconds
d = rs // 86400 #d=days
rs = rs % 86400
h = rs // 3600 #h=hours
rs = rs % 3600
m = rs // (60) #m=minutes
s = rs % (60) #s=seconds
print(y)
print(d)
print(h)
print(m)
print(s)