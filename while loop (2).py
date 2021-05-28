#printing 1-100 numbers ended with 3
no=int(input('enter the no'))
i=no
count=0
while (i<=100):
    print i
    i=i+10
    count=count+1
print 'total count of numbers ended with %d is %d' %(no,count)

#output
#enter the no3
#3
#13
#23
#33
#43
#53
#63
#73
#83
#93
#total count of numbers ended with 3 is 10
