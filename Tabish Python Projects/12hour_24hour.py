
def timeConversion(s):
    print('Time in 12 hour format is: ', s)
    if s[-2::] == "AM":
        if s[:2:] == str(12):
            return '00' + s[2:-2]
        
        return s[0:-2]
    else:
        if s[:2:] == str(12):
            return '12' + s[2:-2]
        x = 13
        for i in range(1,13):
            if i<10:
                j = '0' + str(i)
            else:
                j = str(i)
            if s[:2] == j:
                return str(x) + s[2:-2]
            x+=1

print('Time in 24 hour format is: ', timeConversion('11:59:59PM'))