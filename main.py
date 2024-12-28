def isPowerOf8(x):
    if(x == 0):
        return False
    else:
        while(x % 8 == 0):
            x /= 8
    return (x==1)
x = int(input("Enter your number:"))
if(isPowerOf8(x)):
    print(x,"is a power of 8")
else:
    print(x,"is not a power of 8")