import string
import random
pgen=None
while True:
    passlen=int(input("enter the length of password"))
    if(passlen<6):
        print("password length cant be less than 6")
    else:
        break
s=string.ascii_lowercase+string.ascii_uppercase+string.digits+ \
string.punctuation
pgen="".join(random.sample(s,passlen))
print(pgen)
pgen1=random.sample(string.ascii_uppercase,1)
pgen2=random.sample(string.ascii_lowercase,1)
pgen3=random.sample(string.digits,1)
pgen4=random.sample(string.punctuation,1)
lst_password=[]
lst_password=lst_password+pgen1
lst_password=lst_password+pgen2
lst_password=lst_password+pgen3
lst_password=lst_password+pgen4
lst_password.extend(random.sample(s,(passlen-4)))
random.shuffle(lst_password)
print(lst_password)
temp=''
for i in lst_password:
    temp=temp+str(i)
print(temp)



