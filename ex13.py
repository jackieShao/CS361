import re

file = open('emails.txt', "r")
file = file.read()

eAddress = re.findall(r'([\w\d\.\"-]+@[\w\d\.-]+(\.com|\.es|\.uk))', file)
print (eAddress)

