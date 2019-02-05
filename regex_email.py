import re
str1="please contact info@gmail.co.in for praveen.nsic@gmail.com assistance preetarsh@gmail.com and a@b.co.in"
addresses=re.findall(r'[\w\.-]+@[\w\.-]+',str1)
print(addresses)

