import re
print("welcome to mail validator")

inputem=input("\n Enter your email : ")

patter=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
if  re.fullmatch(patter,inputem):
    print('Valid ')
else :
    print("Not Valid emil")