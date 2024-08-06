text = "hello world"
for char in text:
    if char in "aeiou":
        continue
    print(char)
    """ 
    Kathmnadu => 9, ->k,a,t,h,m,a,n,d,u
    output-> k,t,h,m,n,d

    """