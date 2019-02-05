def addfive(x):
    temp=x+5
    return temp

nums=[11,22,33,44,55]
result=list(map(addfive,nums))
print(nums)
print(result)

#lambda
re=list(map(lambda x:x+5,nums))
print(nums)
print(re)
