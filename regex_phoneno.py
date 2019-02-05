import re
phone="2004-bc959-a559 ### this is phone no."
print(phone)
#delete python style comments
num=re.sub(r'#.*$',"",phone)
print("phone num: ",num)
#remove anything other than digits
num=re.sub(r'\D',"",num)
print("phone num: ",num)
