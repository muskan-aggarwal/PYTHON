import re
pattern=r"spam"
str1="this is spam"
str2="spamsss is here"
if re.match(pattern,str1):#str2
    print("match found")
else:
    print("not found")
if re.search(pattern,str1):#str2
    print("match found")
else:
    print("not found")
