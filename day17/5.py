# Largest Number Among Three Numbers

def checkNum(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c

ans = checkNum(1,9,3)
print(ans)
    