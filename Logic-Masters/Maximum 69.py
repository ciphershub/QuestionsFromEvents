#Approach using string conversion
def maximum69Number (num: int):
    a = list(str(num))
    for i in range(len(a)):
        if a[i] == "6":
            a[i] = "9"
            break
    return int(''.join(a))

#Integer Approach
def maximum69Number (self, num):
    i = 0
    temp = num
    sixind = -1
    while(temp>0):
        if(temp%10 == 6):
            sixind = i
        temp /= 10
        i += 1
    if(sixind == -1):
        return num
    else:
        return(num + 3*(10**sixind))
