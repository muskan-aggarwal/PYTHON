def printTwoCharUp(symbol,n):
    ch='.'
    space=0
    chars=n
    m=1
    if(n%2==0):
        line=n//2
    else:
        line=(n//2)+1
    count=1
    while(count<line):
        print(ch*((chars//2)-space),symbol*m,ch*((chars//2)-space))
        space+=1
        m+=2
        count+=1
    return
def printTwoCharDown(symbol,n):
    ch='.'
    space=0
    chars=n
    if(n%2==0):
        line=n//2
    else:
        line=(n//2)+1
    count=1
    while(count<=line):
        print(ch*space,symbol*chars,ch*space)
        space+=1
        chars-=2
        count+=1
    return
printTwoCharUp('*',8)
printTwoCharDown('*',8)
